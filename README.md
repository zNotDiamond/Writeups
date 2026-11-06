<div align="center">

# Cybersecurity writeups from four total platforms

</div>

## Platforms

| Platform                                                       | Organisation                                                                                                                           | Folder                                                         |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------- |
| [TryHackMe](https://tryhackme.com/p/zNotDiamond)               | **Rooms**: Walkthroughs that are guided labs/lessons teaching a specific cyber topic.<br>**Challenges**: Rooms with little to no help. | `TryHackMe/Rooms` <br><br>`TryHackMe/Challenges`           |
| [Root-Me](https://www.root-me.org/zNotDiamond-1123460?lang=en) | Separated into **categories** (Cryptanalyse, Web-Client...)                                                                            | `Root-Me/Cryptanalyse`, `Root-Me/Web-Client` (...)             |
| [CryptoHack](https://cryptohack.org/user/zNotDiamond)          | Separated by the **topic** (Elliptic Curves, Diffie-Helman...)                                                                         | `Cryptohack/Elliptic Curves`, `Cryptohack/Diffie-Helman` (...) |
| [Hackropole](https://hackropole.fr)                            | Separated into **categories** (same thing as Root-Me)                                                                                  | `Hackropole/Cryptanalyse`, `Hackropole/Forensics` (...)        |

## Notes

The more complicated the challenge, the more detailed the writeup will be. For instance, simple TryHackMe rooms have a writeup associated to them with simply the questions and answers with little to no explanation. While for some CryptoHack rooms, with deep mathematics background, then the writeup (`flag.md`) will have a deep explanation. 

## Structure

(Made with [Repotree](https://ascii-repotree.vercel.app/generator))
```
├── .meta
├── Cryptohack
├── Hackropole
├── Info
├── Root-Me
├── Tools
├── TryHackMe
├── .gitattributes
└── .gitignore
```

Each platform folder is split by category, then by the name of the challenge. A challenge folder holds the script(s) used to solve it, and a `flag.md` file that has the writeup and the flag inside.

`Info/` and `Tools/` gather general notes from myself in order to solve some rooms. 

`.meta/` contains the scripts and assets that keep this repository clean. Cf below.

## Flags

Root-Me and HackTheBox don't allow publishing flags and solutions. Therefore, the `flag.md` (even `flag.png`) files of these two platforms are never published as they are.

Redaction happens locally, before each commit, through Git clean filters. The real flag stays on my PC and the repository only receives a placeholder.

| Filter        | Applies to                           | Effect                                                                                   |
| :------------ | :----------------------------------- | :--------------------------------------------------------------------------------------- |
| `redactflag`  | `flag.md` in Root-Me and HackTheBox  | Replaced by `.meta/flag-placeholder.md` w/ `nope.gif`                                    |
| `redactimage` | `flag.png` in Root-Me and HackTheBox | Replaced by `.meta/assets/nope.gif`                                                      |
| `striptags`   | every `.md` file                     | Removes the Obsidian tag (I use tags to organize myself inside Obsidian) line at the top |

The filters are declared in `.gitattributes` and implemented in `.meta/scripts/`.

## Setup

Filters are stored in the local Git config, so they are not part of a clone. To reproduce the setup:

```sh
git config filter.redactflag.clean  "python3 .meta/scripts/redact-flag.py"
git config filter.redactimage.clean "python3 .meta/scripts/redact-image.py"
git config filter.striptags.clean   "python3 .meta/scripts/strip-tags.py"

git config filter.redactflag.smudge  cat
git config filter.redactimage.smudge cat
git config filter.striptags.smudge   cat

git config filter.redactflag.required  true
git config filter.redactimage.required true
git config filter.striptags.required   true
```

N.B: The `required` option makes Git refuse to add a file if a filter fails, instead of committing it unfiltered.

