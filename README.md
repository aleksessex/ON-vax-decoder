# Verify Ontario Vaccine Passport Decoder

A simple decoder to view and digitally verify the contents of Ontario's enhanced COVID-19 vaccine passport PDF. The decoder does two things:

1. It extracts and prints the PII and vax info contained in the QR code. You can see sample output in `samples/sample_output`.
2. It checks and verifies the digital signature contained in the QR code

Run the decoder as follows:

```
python on_vax_decode.py <path_to_pdf>
```
Ontario residents can download their enhanced (digitally signed) vaccine passport PDF here: [https://covid19.ontariohealth.ca/](https://covid19.ontariohealth.ca/)

## So What?

The main purpose of this project is to provide **transparency** to the Ontario vaccine passport system in the context of personally identifiable information. Ontarians are required to show these QR codes to businesses. These interactions are no longer necessarily ephemeral; a digital device scans the QR code opening the door to mass information retention and potential abuse.  

The Ontario vaccine certificates contain your _full name_ and _date of birth_, which is sufficient to uniquely indentify most individuals. When you show your passport, this (effectively) unique identifier is paired with a time and location.

In addition to adding digital signatures to vaccine certificates, the government is provides its own verifier app. So having independent verifiers could prove useful in certain scenarios, for example:

1. **A buggy app**. You download your passport but the Verify Ontario app shows the signature is invalid. Independent verifiers can confirm whether the signature really is invalid, or the app itself is wrong.
2. **A vulnerable app**. Hackers discover a signature bypass exploit in the Verify Ontario app. Independent verifiers can confirm an invalid signature really is invalid.
3. **Dubious govt claims**. You discover the govt is including some questionable personally identifiable information in the QR code. The government spokesperson says "oh no, we don't include _that_." An independent verifier could demonstrate otherwise.

## Notes and References

- Ontario's vaccine passport is based on the SMART Health Cards (SMT) Framework:
[https://github.com/smart-on-fhir/health-cards](https://github.com/smart-on-fhir/health-cards)
- The QR code in `samples/sample_intput.pdf` is provided for visualization purposes. It does not contain a valid [JSON Web Signature](https://datatracker.ietf.org/doc/html/rfc7515) (JWS).
- We use the signature verification key [found here](https://prd.pkey.dhdp.ontariohealth.ca/.well-known/jwks.json)
- You can verify the signatures with the Verify Ontario app available at: [https://covid-19.ontario.ca/verify](https://covid-19.ontario.ca/verify)

## External Dependencies (MacOS)

pdf2image requires [poppler](http://macappstore.org/poppler/)

```
brew install poppler
```

pyzbar requires [zbar](https://formulae.brew.sh/formula/zbar)

```
brew install zbar
```









