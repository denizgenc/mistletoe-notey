mistletoe-notey
===============

This is based on Mi Yu's mistletoe, which is an extensible, CommonMark compliant Markdown parser in
pure Python. See it here: https://github.com/miyuchina/mistletoe

misteltoe-notey, however, does not comply with CommonMark. It parses my own form of Markdown that's
more in line with how I take plaintext notes. I don't have a specification or a real name for it
(I'm thinking of calling it Notey Markdown, hence the name of this repo), so this is pretty much the
only place you can find out about it (and, I guess, the reference implementation).

Differences from CommonMark
---------------------------
The following two changes go hand in hand:

- Complete removal of indented code blocks: https://spec.commonmark.org/0.29/#indented-code-blocks
- Allowing an initial list item to be indented with 4 spaces (which causes no issue since indented
  code blocks don't exist any longer)
    - I could potentially make this change for HTML blocks and block quotes, but I don't use those.

For some reason, mistletoe by default seems to enable Github Flavored Markdown (GFM) extensions
(the one I've noticed is strikethrough), so you can add those to the pile too.

Motivation
----------
tl;dr: read this Twitter thread: https://twitter.com/denizgenc_623/status/1179775450878492676

When I take notes, they look like this:
```
I have a point that is made
    - And then I might start writing related points as a list with a 4 space indent
    - I do this to more clearly distinguish these lists as "children" of the initial point
    - And the 4 space indent is because I'm a Python programmer with a softtabstop of 4
```

However, when I do this with CommonMark compliant Markdown implementations (which includes GFM),
as an indented code block (i.e. a line starting with 4 spaces) cannot interrupt a paragraph (see
https://spec.commonmark.org/0.29/#example-83), it collapses the list items into the "parent" line.

This makes
```
These
    - sorts
    - of
    - lists
```
render as:

These
    - sorts
    - of
    - lists

(see the source for the above "line" if you don't believe me).

This has potential solutions, the simplest of which is to use an indent with 2 spaces (or 3 spaces,
if you're feeling spicy) when making lists.
```
This
  - Works as
  - you might expect
```
renders:

This
  - Works as
  - you might expect

But I don't want to change my softtabstop for plaintext or Markdown files. So because, for some
reason, I felt kind of stubborn about this, I decided to create my own "spec". /shrugs

**Q:** Where are you going to use this? If you want your Markdown notes rendering somewhere, it 
       most definitely is going to use something close to CommonMark, so you won't be able to use
       this and you'll end up having to reformat your notes regardless.  
**A:** Yes, this is kind of pointless (unless I make my own website and with a templating engine
       based on Markdown, and then I have an excuse to swap out the parser in that with this one).
       However, now that I've done this, I'm more motivated to make a "transpiler" (for plaintext,
       lmao) that converts my not-quite-Markdown to proper Markdown. Everything is possible.
