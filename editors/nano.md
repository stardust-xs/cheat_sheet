<!-- markdownlint-disable MD033 MD041 -->
# Nano :pencil:

This cheat sheet covers the usage of [**GNU nano**](https://www.nano-editor.org/) editor.<br>So basically, nano is a simple text editor written in [**C**](https://en.wikipedia.org/wiki/C_%28programming_language%29) and is shipped with all versions/distros of **Linux** by default.

Nano is installed by default, simple to use and is probably the easiest to learn from all command line editors, so lets get started.

**DISCLAIMER:** There are different ways of carrying out a particular thing in nano but, I'll be explaining the methods that I've been using so far and have proved to be more practical and simple to remember.

## Help

In case you don't want to follow along or want to learn nano by yourselves, you can click **Ctrl + G** to pop up the help menu.<br>The help menu is one-stop solution for all your queries related to nano. But it doesn't cover how you can combine the keystrokes to achieve shortcuts beyond the scope!

**NOTE:** You may see some weird keystroke pairs like **^**, **M-**, **Sh-** or (:arrow_up_small::arrow_forward::arrow_down_small::arrow_backward:).<br>These represent your **Ctrl**, **Alt** or **Esc**, **Shift** and **Directional arrow** keys respectively. Also one thing to note here is the fact that these shortcuts are **not** case-sensitive.<br>Also a side note, it would be much better if you learn the alternate keystrokes as well because if you work on a laptop, you may not have separate keys like **Home**, **End** or **Page Up** and **Page Down** keys.

## Navigations

Although there are couple of ways of navigating through nano, the best and the most obvious way is to use the **directional arrow**<br>keys (:arrow_up::arrow_right::arrow_down::arrow_left:) on your keyboard. Their usage is simple as it can get, use them to move through the characters one by one.<br>The directional arrow keys paired with **Ctrl** key will let you move through the **entire word** (left-right) or through the **entire paragraph** (up-down).

**Ctrl + A** will let you go to the first character of the current line, **Ctrl + E** will let you move to the last character of the current line.<br>The same can be done using **Home** and **End** buttons respectively.

**Alt + \\** (backslash or key above the enter/return) will let you jump to the beginning of the document and **Alt + /** (forward slash or key besides shift) will let you jump to the end. This saves a lot of time when you need to append something to a long document.<br>The same can be performed using **Ctrl + Home** and **Ctrl + End**.

**Page Up** and **Page Down** will let you move a up and down **entire screen** worth of text. This is super useful when you need to navigate midway through a long document. There's another shortcut for this but I don't feel that's intuitive so I'll add it in below table.

## Select, Cut, Copy, Paste and Delete

Well, now you know how to navigate through the document, let's learn how to perform the basic operations like cut-copy-paste.<br>Before jumping on to copy-pasting, we need to first understand how selection works in nano.

### Select

Selecting text in nano has some sort of **liberty*** to it. You can simply select text using your mouse or just using your keyboard. Although both have their perks.

Selecting via **mouse** is quite easy, simply select the text that needs to be copied and **right click** to copy it. Here, you need to understand that this method of copying is different from what nano considers copying. Copying using this method essentially copies text in your system memory buffer (RAM) and not in **nano's buffer** (nano's internal memory). To put it simply, you can use **Ctrl + Shift + C** and **Ctrl + Shift + V** for copy-pasting the text once it is selected by a mouse and use it outside nano as well.

The above method works just fine but has a huge limitation, it can just copy and paste stuff which may not be sufficient for your every use case. To solve this, nano has other ways of selecting text which it calls as "**Marking**" text. So in order to mark the text, you can simply shift click using directional arrow keys like **Shift + (:arrow_up::arrow_right::arrow_down::arrow_left:)**. This starts marking/selecting text character by character.<br>In case you want to mark/select text word by word you can use **Ctrl + Shift + (:arrow_up::arrow_right::arrow_down::arrow_left:)**. This is far better and a faster approach.

Another alternate solution to this is using **Alt + A** to begin marking and then selecting text using the directional arrows, so it looks something like **Alt + A + (:arrow_up::arrow_right::arrow_down::arrow_left:)** for selecting characters or **Alt + A + Ctrl + (:arrow_up::arrow_right::arrow_down::arrow_left:)** for select whole words.

In case you need to select everything (select all), unfortunately there's no official shortcut for this. But we can combine the keystrokes to achieve this as well. Simply navigate to the start of the document, start marking and jump to end of the document.<br>So this looks like this, **Ctrl + Home** followed by **Alt + A** and then **Ctrl + End**.

As a side note, you can do **Alt + A** to stop marking.

### Cut

Cutting text is an essential part of using a text editor. Nano makes cutting easy with **Ctrl + K**. Where **Ctrl + K** cuts entire line and in case you need to cut a portion of a sentence, you need to select text and then cut it. So it looks like **Alt + A + (:arrow_up::arrow_right::arrow_down::arrow_left:)** to select something followed by **Ctrl + K** to cut. Alternate keystroke for cutting is **F9** which feels less intuitive in my opinion.

**NOTE:** Please note that when something is "cut" in nano, it stays in buffer (nano's internal memory) so it cannot be used outside nano.

### Copy

Copying text is similar to cutting. For copying an entire line, use **Alt + 6** and for copying portion of a sentence, do **Alt + A + (:arrow_up::arrow_right::arrow_down::arrow_left:)** to select something followed by **Alt + 6** to copy. Alternate keystroke for pasting is **Alt + Shift + 6** which seems little redundant. Also the copied text stays in buffer and can't be used outside.

In case you need to copy text outside nano, copy text using **Ctrl + Shift + C**.

### Paste

Pasting text is as easy as it gets just do **Ctrl + U**. Pasting will only paste whatever was stored in the buffer. Alternate keystroke for copying is **F10** which again feels less practical on laptops with multi-functional **Fn** keys.

In case you need to paste something from outside nano into nano, then use **Ctrl + Shift + V**.

## Summary

Lets summarize what we know.

| Shortcut | Alternative | Action |
|-|-|-|
| →←↑↓ | Ctrl + F (forward), Ctrl + B (backward), Ctrl + P (+ve axis), Ctrl + N (-ve axis) | Navigate character by character |
| Home, End | Ctrl + A, Ctrl + E | Start of line, End of line |
| Ctrl + Home, Ctrl + End | Alt + \\, Alt + / | Start of document, End of document |
| Page Up, Page Down | Ctrl + Y, Ctrl + V | Scroll entire screen worth of text |
| Shift + (→←↑↓) | Alt + A + (→←↑↓) | Select by characters |
| Ctrl + Shift + (→←↑↓) | Alt + A + Ctrl + (→←↑↓) | Select by words |
| Ctrl + Home → Alt + A → Ctrl + End |  | Select all |
| Ctrl + K | F9 | Cut entire line with line break |
| Alt + A + (→←↑↓) → Ctrl + K | Alt + A + (→←↑↓) → F9 | Cut words/portion of a sentence |
| Alt + 6 | Alt + Shift + 6 | Copy entire line with line break |
| Alt + A + (→←↑↓) → Alt + 6 | Alt + A + (→←↑↓) → Alt + Shift + 6 | Copy words/portion of a sentence |
