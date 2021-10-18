{
    "alg": "ES256",
    "kid": "Nlgwb6GUrU_f0agdYKc77sXM9U8en1gBu94plufPUj8",
    "zip": "DEF"
}
{
    "iss": "https://prd.pkey.dhdp.ontariohealth.ca",
    "nbf": 1634564789.441,
    "vc": {
        "credentialSubject": {
            "fhirBundle": {
                "entry": [
                    {
                        "fullUrl": "resource:0",
                        "resource": {
                            "birthDate": "2000-01-01",
                            "name": [
                                {
                                    "family": "Poutine",
                                    "given": [
                                        "Pierre",
                                        "Robert"
                                    ]
                                }
                            ],
                            "resourceType": "Patient"
                        }
                    },
                    {
                        "fullUrl": "resource:1",
                        "resource": {
                            "lotNumber": "XY1234",
                            "manufacturer": {
                                "identifier": {
                                    "system": "http://hl7.org/fhir/sid/mvx",
                                    "value": "PFR"
                                }
                            },
                            "meta": {
                                "security": [
                                    {
                                        "code": "IAL1.4",
                                        "system": "https://smarthealth.cards/ial"
                                    }
                                ]
                            },
                            "occurrenceDateTime": "2021-05-01",
                            "patient": {
                                "reference": "resource:0"
                            },
                            "performer": [
                                {
                                    "actor": {
                                        "display": "ON, Canada"
                                    }
                                }
                            ],
                            "resourceType": "Immunization",
                            "status": "completed",
                            "vaccineCode": {
                                "coding": [
                                    {
                                        "code": "208",
                                        "system": "http://hl7.org/fhir/sid/cvx"
                                    },
                                    {
                                        "code": "21234000012345",
                                        "system": "http://snomed.info/sct"
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "fullUrl": "resource:2",
                        "resource": {
                            "lotNumber": "XY1234",
                            "manufacturer": {
                                "identifier": {
                                    "system": "http://hl7.org/fhir/sid/mvx",
                                    "value": "PFR"
                                }
                            },
                            "meta": {
                                "security": [
                                    {
                                        "code": "IAL1.4",
                                        "system": "https://smarthealth.cards/ial"
                                    }
                                ]
                            },
                            "occurrenceDateTime": "2021-07-01",
                            "patient": {
                                "reference": "resource:0"
                            },
                            "performer": [
                                {
                                    "actor": {
                                        "display": "ON, Canada"
                                    }
                                }
                            ],
                            "resourceType": "Immunization",
                            "status": "completed",
                            "vaccineCode": {
                                "coding": [
                                    {
                                        "code": "208",
                                        "system": "http://hl7.org/fhir/sid/cvx"
                                    },
                                    {
                                        "code": "21234000012345",
                                        "system": "http://snomed.info/sct"
                                    }
                                ]
                            }
                        }
                    }
                ],
                "resourceType": "Bundle",
                "type": "collection"
            },
            "fhirVersion": "4.0.1"
        },
        "type": [
            "https://smarthealth.cards#health-card",
            "https://smarthealth.cards#immunization",
            "https://smarthealth.cards#covid19"
        ]
    }
}