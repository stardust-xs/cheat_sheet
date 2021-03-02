"""Logging with Miroslava.

This module offers tools that help with logging events.
It relies on the original `logging` module from the standard python
library as Miroslava's logging implementation doesn't intent to change
or modify the existing work put behind the original logging module but
rather adds some* level of simplicity and flexibility that is most
often required in many development scenarios.

Although this module doesn't cover all the quintessential requirements
but rather comes close to meet the end-user's expectations.

Attributes:
    _tty_levels (dict): Dictionary of logging levels and corresponding
        colors for logging.
    _tty_reset (str): Code to reset the TTY color mode to normal.

Todo:
    * Option to disable one-line traceback message.
    * Multiple log rotation options.

"""

import logging
import sys
from logging.handlers import RotatingFileHandler as FileHandler
from os.path import abspath, basename, join, splitext
from typing import IO, Any, Dict, Optional, Tuple, Union

from miroslava.config.internal import (
    LOGGER_DATETIME_FMT,
    LOGGER_EXC_FMT,
    LOGGER_MSG_FMT,
    LOGGER_PATH,
    PATH_SEP,
)
from miroslava.utils.common import Singleton, TTYPalette

__all__ = ["Logger", "Formatter", "StreamHandler"]

# NOTE: Most of the docstring is referenced from the original logging
# module since this logger does not intent to change the behavior of
# the underlying implementation but rather adds some level of simplicity
# and flexibility that is required in most of the development cases.

_tty_levels = {
    logging.CRITICAL: TTYPalette.RED_1,
    logging.ERROR: TTYPalette.DARK_ORANGE,
    logging.WARNING: TTYPalette.YELLOW,
    logging.INFO: TTYPalette.GREEN_1,
    logging.DEBUG: TTYPalette.GREY_50,
    logging.NOTSET: TTYPalette.AQUA,
}

_tty_reset = TTYPalette.DEFAULT


class Formatter(logging.Formatter, metaclass=Singleton):
    """Formatter to convert the LogRecord to text.

    A Formatter need to know how the LogRecord is constructed. It is
    responsible for converting the LogRecord to (usually) a string which
    can be interpreted by either a human or an external system.

    This Formatter class allows uniform formatting across various
    logging levels using the message format provided to it. If None
    is provided, default template would be used.

    The Formatter can be initialized with a format string which makes
    use of knowledge of the LogRecord attributes and thus provides an
    extension for logging the records and traceback information in a
    graceful manner.

    The default formatting template is inspired by the `Spring Boot`
    framework.

    Args:
        log_fmt (str, optional): Logging message format.
            Defaults to `LOGGER_MSG_FMT`.
        date_fmt (str, optional): Logging datetime format. Defaults to
            `LOGGER_DATETIME_FMT`.

    Attributes:
        default_fmt (bool): Whether default format is used or not.
        log_fmt (str): Logging message format.
            Defaults to `LOGGER_MSG_FMT`.
        date_fmt (str): Logging datetime format. Defaults to
            `LOGGER_DATETIME_FMT`.

    See Also:
        logging.Formatter:
            Logging formatter class from standard library.
        miroslava.config.internals:
            Module which holds all the constants used in the Formatter.
        miroslava.utils.common.Singleton:
            A thread-safe implementation of Singleton design pattern.

    """

    def __init__(
        self,
        log_fmt: Optional[str] = None,
        date_fmt: Optional[str] = None,
    ) -> None:
        self.default_fmt = False
        if not log_fmt:
            log_fmt = LOGGER_MSG_FMT
            self.default_fmt = True
        if not date_fmt:
            date_fmt = LOGGER_DATETIME_FMT
        self.log_fmt = log_fmt
        self.date_fmt = date_fmt

    def formatException(self, ei: Tuple) -> str:
        """Format exception information as text.

        Please note that this implementation does not work directly.
        The standard `logging.Formatter()` is required for creating
        the `str` format of the logged record which adds an unnecessary
        `\\n` to the output which needs to be skipped.

        Args:
            ei (_SysExcInfoType): Exception information.

        Note:
            _SysExcInfoType is Tuple(type, BaseException, TracebackType)

        Returns:
            str: Formatted exception information.

        """
        exc_cls, exc_msg, exc_tbk = ei
        exc_fnc = exc_tbk.tb_frame.f_code.co_name
        exc_obj = "on" if exc_fnc == "<module>" else f"in {exc_fnc}() on"
        exc_tbk = exc_obj, exc_tbk.tb_lineno
        return LOGGER_EXC_FMT.format(exc_cls.__name__, exc_msg, *exc_tbk)

    def formatPath(self, path: str, fnc: str, limit: int = 27) -> str:
        """Format path with module-like structure.

        This formatting function ensures that the `pathname` attribute
        follows the standard pattern similar to that of `Spring Boot`
        framework.

        If the `Logger` is called from a module, the absolute path of
        the module would be considered and if triggered via the shell or
        the interpreter (stdin), `shell` would be returned.

        Args:
            path (str): Pathname of the logged event.
            fnc (str): Function (callable instance) of the logged event.

        Returns:
            str: Formatted pathname value.

        """
        if path == "<stdin>":
            return "shell"
        path = path[path[0] == PATH_SEP : -3].replace(PATH_SEP, ".")
        if fnc != "<module>":
            path += f".{fnc}()"
        if len(path) > limit:  # maximum limit
            path = "..." + path[-limit:]
        return path

    def format(self, record: logging.LogRecord) -> str:
        """Format the specified record as text.

        If there is exception information, it is formatted using the
        `formatException()` and replaced with the original message.

        Args:
            record (LogRecord): Instance of an event being logged.

        Returns:
            str: Formatted log output.

        """
        if self.default_fmt:
            record.caller = self.formatPath(record.pathname, record.funcName)
        if record.exc_info:
            record.msg = self.formatException(record.exc_info)
            record.exc_info = record.exc_text = None
        return logging.Formatter(self.log_fmt, self.date_fmt).format(record)


class StreamHandler(logging.StreamHandler, metaclass=Singleton):
    """Add colors to the TTY interface.

    A handler class which writes logging records, color formatted, to
    a stream. Note that this class does not close the stream, as
    sys.stdout or sys.stderr may be used.

    Args:
        stream (IO): IO stream. Defaults to sys.stdout.
        only_level (bool): Whether to colorize only the levels.
            Defaults to True.
        **kwargs: Keyword list of log attrs and colors.

    Attributes:
        only_level (bool): Whether to colorize only the levels.
            Defaults to True.
        **kwargs: Keyword list of log attrs and colors.

    Returns:
        str: Color formatted log output.

    See Also:
        logging.StreamHandler:
            Logging handler class from standard library.
        miroslava.utils.common.Singleton:
            A thread-safe implementation of Singleton design pattern.
        miroslava.config.common.TTYPalette:
            Class which provides color codes for a TTY interface.

    """

    def __init__(
        self,
        stream: Optional[IO[str]] = sys.stdout,
        *,
        only_level: bool = True,
        **kwargs: Dict[str, str],
    ) -> None:
        self.only_level = only_level
        self.kwargs = {k: getattr(TTYPalette, v) for k, v in kwargs.items()}
        super().__init__(stream=stream)

    def format(self, record: logging.LogRecord) -> str:
        """Format the attrs with colors.

        Args:
            record (LogRecord): Instance of an event being logged.

        Returns:
            str: Color formatted log output.

        """
        out = logging.StreamHandler.format(self, record)
        if self.only_level:
            out = out.replace(
                record.levelname,
                _tty_levels[record.levelno] + record.levelname + _tty_reset,
            )
            return out
        for key, value in self.kwargs.items():
            if hasattr(record, key):
                attr = str(getattr(record, key))
                out = out.replace(attr, value + attr + _tty_reset)
        return out


class Logger(logging.LoggerAdapter):
    """Logger for logging events.

    Logger offers flexible logging using the different arguments that
    are passed to it. If nothing is supplied, the default settings are
    used. Logger relies on its own log message format as it seems to
    provide all the essential information by default. However, as said
    above the default behavior can be overridden using the arguments.

    Logger allows user to set a minimum logging level which ensures all
    the events equal and above the set level are logged. Logger enables
    logging for a module or for the entire process and offers options
    to colorize the logged attributes as well.

    Args:
        name (str): Root instance for logging. Defaults to None.
        level (int, str, optional): Minimum logging level to record.
            Defaults to `logging.INFO`.
        file (str, optional): Output log file pathname. Defaults to
            module name which calls the logger.
        log_fmt (str, optional): Logging message format.
            Defaults to `LOGGER_MSG_FMT`.
        date_fmt (str, optional): Logging datetime format. Defaults to
            `LOGGER_DATETIME_FMT`.
        only_level (bool): Whether to colorize only the levels.
            Defaults to True.
        filesize (float, int): Maximum size the output log file can be
            in bytes. Defaults to 10 MB.
        backups (int): Maximum backups to retain after the rollover.
            Defaults to 5.
        extra (dict, optional): Adds extra contextual information to the
            log messages.
        **attrs: Keyword list of log attributes and colors.


    Attributes:
        ext (str): Log file extension.
        logger (logging.Logger): Logger object which logs the events.
        extra (dict): Adds extra contextual information to the log
            messages.

    Notes:
        By default, the output log file if created normally grows
        indefinitely. You can specify particular value of `filesize`
        and `backups` to allow this file to rollover at a predetermined
        size.

        The rollover happens whenever the current log file is nearly
        `filesize` in length. If the `backups` is >= 1, the system will
        successively create new files with the same pathname as the
        base file, but with the extensions ".1", ".2", etc. appended to
        it. For example, with `backups` of 5 and output log name of
        "xa.log", you would get "xa.log", "xa.log.1", "xa.log.2", ...
        through "xa.log.5".

        If `filesize` is zero, rollover never occurs.

    Examples:
        >>> logger = Logger()
        >>> def f():
        ...     try:
        ...         5 / 0
        ...     except Exception as exc:
        ...        logger.exception(exc)
        ...
        >>> f()
        Apr 11, 2020...  ERROR [...]  shell:004 - ZeroDivisionError: ...
        >>>

    See Also:
        logging.LoggerAdapter:
            An adapter for loggers which makes it easier to specify
            contextual information in logging output.
        logging.handlers.RotatingFileHandler:
            Handler for logging to a set of files, which switches from
            one file to the next when the current file reaches a
            certain size.
        miroslava.utils.logger.Formatter:
            Formatter class to convert a LogRecord to text.
        miroslava.utils.logger.StreamHandler:
            Class to add colors to the TTY interface.

    """

    ext = ".log"

    def __init__(
        self,
        name: Optional[str] = None,
        level: Optional[Union[int, str]] = None,
        file: Optional[str] = None,
        log_fmt: Optional[str] = None,
        date_fmt: Optional[str] = None,
        only_level: bool = True,
        filesize: Union[float, int] = 10e6,
        backups: int = 5,
        extra: Optional[Dict[str, Any]] = None,
        **attrs: Dict[str, str],
    ) -> None:
        formatter = Formatter(log_fmt, date_fmt)
        stream = StreamHandler(only_level=only_level, **attrs)
        stream.setFormatter(formatter)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level if level else logging.INFO)
        self.logger.addHandler(stream)
        if file is None:
            try:
                caller = basename(abspath(sys.modules["__main__"].__file__))
                file = join(LOGGER_PATH, (splitext(caller)[0] + self.ext))
            except AttributeError:
                file = False
        if file is not False:
            file = FileHandler(file, maxBytes=filesize, backupCount=backups)
            file.setFormatter(formatter)
            self.logger.addHandler(file)
        self.extra = extra if extra else {}

    def debug(self, msg: Any) -> None:
        """Log message with `DEBUG` level severity."""
        for line in str(msg).splitlines():
            self.logger.debug(line, extra=self.extra, stacklevel=2)

    def info(self, msg: Any) -> None:
        """Log message with `INFO` level severity."""
        for line in str(msg).splitlines():
            self.logger.info(line, extra=self.extra, stacklevel=2)

    def warning(self, msg: Any) -> None:
        """Log message with `WARNING` level severity."""
        for line in str(msg).splitlines():
            self.logger.warning(line, extra=self.extra, stacklevel=2)

    def error(self, msg: Any) -> None:
        """Log message with `ERROR` level severity."""
        for line in str(msg).splitlines():
            self.logger.error(line, extra=self.extra, stacklevel=2)

    def critical(self, msg: Any) -> None:
        """Log message with `CRITICAL` level severity."""
        for line in str(msg).splitlines():
            self.logger.critical(line, extra=self.extra, stacklevel=2)

    def exception(self, msg: Any) -> None:
        """Log exception with traceback."""
        self.logger.error(msg, exc_info=True, extra=self.extra, stacklevel=2)

    fatal = critical
    warn = warning
