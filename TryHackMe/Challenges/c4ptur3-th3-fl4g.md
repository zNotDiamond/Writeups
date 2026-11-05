This room is a pure encoding and steganography gauntlet — no exploitation, no shells, just layer after layer of ciphers, spectrograms, and hidden data. It’s a perfect example of why every decoded string deserves a second look before assuming the puzzle is solved. Working through ten stacked encodings and three separate steganography techniques makes for a satisfying full clear.

## 1. Translation & Shifting

The first task worked through a chain of ten separate encodings, each one revealing a short message once decoded correctly.

The opening challenge used simple leetspeak substitution:

```
c4n y0u c4p7u23 7h3 f149?
```

Flag: `Can you capture the flag?`

From there, the encodings escalated in complexity. Straight binary decoded to a plain sentence:

Flag: `lets try some binary out!`

Base32 decoding produced the next answer in the sequence, followed by Base64:

Flag: `Each Base64 digit represents exactly 6 bits of data.`

Hexadecimal (Base16) came next:

Flag: `hexadecimal or base16?`

ROT13 and ROT47 followed, each a variant of the classic Caesar shift but operating over a wider character set for ROT47:

Flag: `Rotate me 13 places!`

Flag: `You spin me right round baby right round (47 times)`

Morse code and Binary-Coded Decimal (BCD) rounded out the individual encodings:

Flag: `telecommunication encoding`

Flag: `Unpack this BCD`

The final challenge in this task stacked four encodings on top of each other — Base64, then Morse code, then binary, then ROT47, then decimal — requiring each layer to be peeled off in the correct order before the plaintext emerged.

Flag: `Let’s make this a bit trickier…`

I worked through the chain using a mix of online decoders (codebeauty.org, dcode.fr, base64decode.org) and manual verification at each step, since guessing the wrong encoding for a given layer produces garbage output that looks nothing like a legitimate next stage.

When a decoded output still looks like nonsense, don’t assume the puzzle is broken — try feeding it into a different decoder before giving up, since many encodings produce output that superficially resembles other formats.

## 2. Spectrograms

This task hid its flag inside the frequency data of an audio file rather than its waveform. I loaded the provided .wav file into Sonic Visualiser and added a spectrogram layer to visualize frequency content over time.

Result: text spelled out visually across the frequency spectrum, readable directly from the spectrogram display.

![[Pasted image 20261102214803.png]]

Flag: `Super Secret Message`

Audio steganography that hides text in a spectrogram relies entirely on the assumption that nobody will actually look at the frequency domain — a basic spectrogram tool defeats it instantly.

## 3. Steganography

The third task hid its answer inside a JPEG using classic LSB steganography. I extracted it with steghide.

```
steghide extract -sf stegosteg.jpg
```

Result: hidden data extracted successfully.

![[Pasted image 20261102214820.png]]
Flag: `SpaghettiSteg`

Steghide extraction without a passphrase works whenever the file was embedded without one — always try a blank passphrase first before assuming a password is required.

## 4. Security Through Obscurity

The final task looked like another steganography challenge at first, but steghide and unzip both came up empty. Instead of assuming a more advanced tool was needed, I tried the simplest possible approach and just read the raw file content.

```
cat meme.jpg
```

Result: readable text sitting in plain view at the end of the file, appended directly onto the image data rather than embedded through any real steganographic technique.


The output revealed a referenced filename:
![[Pasted image 20261102214836.png]]


Flag: `hackerchat.png`

Continuing to read through the file’s raw content uncovered a second hidden string:

Flag: `AHH_YOU_FOUND_ME!`

Appending plaintext to the end of an otherwise valid image file isn’t steganography — it’s obscurity. Any tool that simply reads the file’s raw bytes, including cat, strings, or a hex editor, defeats it immediately.

## Lab questions

Task 1, Q1 Decode the leetspeak string: `Can you capture the flag?`

Task 1, Q2  Decode the binary string: `lets try some binary out!`

Task 1, Q3  Decode the Base32 string (decoded string — value not recorded in original notes)

Task 1, Q4  Decode the Base64 string: `Each Base64 digit represents exactly 6 bits of data.`

Task 1, Q5  Decode the hexadecimal string: `hexadecimal or base16?`

Task 1, Q6  Decode the ROT13 string: `Rotate me 13 places!`

Task 1, Q7  Decode the ROT47 string: `You spin me right round baby right round (47 times)`

Task 1, Q8  Decode the Morse code string: `telecommunication encoding`

Task 1, Q9  Decode the BCD string: `Unpack this BCD`

Task 1, Q10  Decode the multi-layer string (Base64 → Morse → Binary → ROT47 → Decimal): `Let’s make this a bit trickier…`

Task 2  What does the spectrogram reveal? `Super Secret Message`

Task 3  Extract the hidden data from stegosteg.jpg: `SpaghettiSteg`

Task 4, Q1  First filename found in meme.jpg: `hackerchat.png`

Task 4, Q2  Hidden text found in meme.jpg: `AHH_YOU_FOUND_ME!`
