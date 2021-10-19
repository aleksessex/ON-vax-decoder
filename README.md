# Verify Ontario Vaccine Passport Decoder

A simple decoder to view and digitally verify the contents of Ontario's enhanced COVID-19 vaccine passport PDF. The decoder does two things:

1. It extracts and prints the PII and vax info contained in the QR code. You can see sample output in `samples/sample_output`.
2. It checks and verifies the digital signature contained in the QR code

Run the decoder as follows:

```
python on_vac_decode.py <path_to_pdf>
```
Ontario residents can download their enhanced (digitally signed) vaccine passport PDF here: [https://covid19.ontariohealth.ca/](https://covid19.ontariohealth.ca/)

## Notes and References

- Ontario's vaccine passport is based on the SMART Health Cards (SMT) Framework:
[https://github.com/smart-on-fhir/health-cards](https://github.com/smart-on-fhir/health-cards)
- The QR code in `samples/sample_intput.pdf` is provided for visualization purposes. It does not contain a valid [JSON Web Signature](https://datatracker.ietf.org/doc/html/rfc7515) (JWS).
- Uses the signature verification key [found here](https://prd.pkey.dhdp.ontariohealth.ca/.well-known/jwks.json)
- You can verify the signatures with the Verify Ontario app available at: [https://covid-19.ontario.ca/verify](https://covid-19.ontario.ca/verify)





