# data.py

DATA_STORE = [
    {
        "csam": {
            "csamId": "CSAM-01",
            "csamName": "Joe Smith",
            "csamEmail": "joesmith@microsoft.com",
            "customers": [
                {
                    "customerName": "Contoso",
                    "tpId": "100001",
                    "industryBusinessSegment": "ISV",
                    "regionAssociatedWithTPID": "Americas",
                    "regionMCSAPWillSupport": "Americas",
                    "workingLanguages": ["English", "French"],
                    "keyTechnologies": ["Databricks", "Azure Networking"],
                    "azureCloudFootprint": "Commercial Cloud",
                    "multiCloudStrategy": ["Azure", "GCP"],
                    "criticalProdSubs": "On next Excel Sheet",
                    "summaryOfCustomerBusiness": "Global cloud and enterprise software provider.",
                    "otherPrograms": ["S500", "HotDL"],
                    "csatCustomerSentiment": "CSAT: 3.9",
                    "incidentSupportData": "35 cases (2 Sev1, 8 SevA, 12 SevB, 13 SevC)",
                    "incidentCorrelationData": "Databricks incidents dominant",
                    "sentimentImpactFactors": ["Cold Handovers"],
                    "whyPurchasedMCSAP": "Poor Unified Support experience",
                    "msftContacts": {
                        "csam": "joesmith@microsoft.com",
                        "ae": "janedoe@microsoft.com"
                    },
                    "customerContacts": {
                        "leadership": [
                            {
                                "name": "Ethan Caldwell",
                                "email": "ethan.caldwell@contoso.com"
                            }
                        ],
                        "operations": [
                            {
                                "name": "Harper Blume",
                                "email": "harper.blume@contoso.com"
                            }
                        ]
                    },
                    "subscriptions": [
                        {
                            "subscriptionId": "sub-001",
                            "subscriptionName": "Prod-1"
                        },
                        {
                            "subscriptionId": "sub-002",
                            "subscriptionName": "Prod-2"
                        }
                    ],
                    "preAedMirp": "Attached File"
                },
                {
                    "customerName": "Fabrikam",
                    "tpId": "100002",
                    "industryBusinessSegment": "Retail",
                    "regionAssociatedWithTPID": "EMEA",
                    "regionMCSAPWillSupport": "EMEA",
                    "workingLanguages": ["English", "German"],
                    "keyTechnologies": ["Azure SQL", "Power BI"],
                    "azureCloudFootprint": "Commercial Cloud",
                    "multiCloudStrategy": ["Azure"],
                    "criticalProdSubs": "On next Excel Sheet",
                    "summaryOfCustomerBusiness": "Retail enterprise focused on omnichannel sales.",
                    "otherPrograms": ["Retail500"],
                    "csatCustomerSentiment": "CSAT: 4.1",
                    "incidentSupportData": "18 cases",
                    "incidentCorrelationData": "Power BI related issues",
                    "sentimentImpactFactors": ["Escalation delays"],
                    "whyPurchasedMCSAP": "Need proactive support",
                    "msftContacts": {
                        "csam": "joesmith@microsoft.com",
                        "ae": "janedoe@microsoft.com"
                    },
                    "customerContacts": {
                        "leadership": [
                            {
                                "name": "Oliver Braun",
                                "email": "oliver.braun@fabrikam.com"
                            }
                        ],
                        "operations": []
                    },
                    "subscriptions": [
                        {
                            "subscriptionId": "sub-003",
                            "subscriptionName": "Retail-Core"
                        }
                    ],
                    "preAedMirp": "Attached File"
                },
                {
                    "customerName": "Northwind",
                    "tpId": "100003",
                    "industryBusinessSegment": "Manufacturing",
                    "regionAssociatedWithTPID": "APAC",
                    "regionMCSAPWillSupport": "APAC",
                    "workingLanguages": ["English"],
                    "keyTechnologies": ["Azure IoT", "Synapse"],
                    "azureCloudFootprint": "Commercial Cloud",
                    "multiCloudStrategy": ["Azure", "AWS"],
                    "criticalProdSubs": "On next Excel Sheet",
                    "summaryOfCustomerBusiness": "Smart manufacturing solutions provider.",
                    "otherPrograms": ["SmartFactory"],
                    "csatCustomerSentiment": "CSAT: 3.6",
                    "incidentSupportData": "22 cases",
                    "incidentCorrelationData": "IoT related incidents",
                    "sentimentImpactFactors": ["RCA delays"],
                    "whyPurchasedMCSAP": "Operational stability",
                    "msftContacts": {
                        "csam": "joesmith@microsoft.com",
                        "ae": "janedoe@microsoft.com"
                    },
                    "customerContacts": {
                        "leadership": [
                            {
                                "name": "Rajiv Mehta",
                                "email": "rajiv.mehta@northwind.com"
                            }
                        ],
                        "operations": []
                    },
                    "subscriptions": [
                        {
                            "subscriptionId": "sub-004",
                            "subscriptionName": "Manufacturing-Prod"
                        }
                    ],
                    "preAedMirp": "Attached File"
                },
                {
                    "customerName": "AdventureWorks",
                    "tpId": "100004",
                    "industryBusinessSegment": "E-Commerce",
                    "regionAssociatedWithTPID": "Americas",
                    "regionMCSAPWillSupport": "Americas",
                    "workingLanguages": ["English", "Spanish"],
                    "keyTechnologies": ["AKS", "Azure Front Door"],
                    "azureCloudFootprint": "Commercial Cloud",
                    "multiCloudStrategy": ["Azure"],
                    "criticalProdSubs": "On next Excel Sheet",
                    "summaryOfCustomerBusiness": "Global e-commerce platform.",
                    "otherPrograms": ["ECom100"],
                    "csatCustomerSentiment": "CSAT: 4.3",
                    "incidentSupportData": "12 cases",
                    "incidentCorrelationData": "AKS upgrade issues",
                    "sentimentImpactFactors": ["Upgrade downtime"],
                    "whyPurchasedMCSAP": "Business critical workloads",
                    "msftContacts": {
                        "csam": "joesmith@microsoft.com",
                        "ae": "janedoe@microsoft.com"
                    },
                    "customerContacts": {
                        "leadership": [
                            {
                                "name": "Laura Chen",
                                "email": "laura.chen@adventureworks.com"
                            }
                        ],
                        "operations": []
                    },
                    "subscriptions": [
                        {
                            "subscriptionId": "sub-005",
                            "subscriptionName": "ECom-Prod"
                        }
                    ],
                    "preAedMirp": "Attached File"
                },
                {
                    "customerName": "Tailspin Toys",
                    "tpId": "100005",
                    "industryBusinessSegment": "Consumer Goods",
                    "regionAssociatedWithTPID": "EMEA",
                    "regionMCSAPWillSupport": "EMEA",
                    "workingLanguages": ["English"],
                    "keyTechnologies": ["App Service", "Cosmos DB"],
                    "azureCloudFootprint": "Commercial Cloud",
                    "multiCloudStrategy": ["Azure"],
                    "criticalProdSubs": "On next Excel Sheet",
                    "summaryOfCustomerBusiness": "Consumer goods manufacturer using cloud-native apps.",
                    "otherPrograms": ["CG200"],
                    "csatCustomerSentiment": "CSAT: 3.8",
                    "incidentSupportData": "16 cases",
                    "incidentCorrelationData": "Cosmos DB throughput",
                    "sentimentImpactFactors": ["Capacity planning"],
                    "whyPurchasedMCSAP": "Architectural guidance",
                    "msftContacts": {
                        "csam": "joesmith@microsoft.com",
                        "ae": "janedoe@microsoft.com"
                    },
                    "customerContacts": {
                        "leadership": [
                            {
                                "name": "Martin Vogel",
                                "email": "martin.vogel@tailspin.com"
                            }
                        ],
                        "operations": []
                    },
                    "subscriptions": [
                        {
                            "subscriptionId": "sub-006",
                            "subscriptionName": "Consumer-Prod"
                        }
                    ],
                    "preAedMirp": "Attached File"
                }
            ]
        }
    }
]

def get_data():
    return DATA_STORE
