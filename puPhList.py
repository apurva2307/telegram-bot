def getPUList():
    return [
        "PU1",
        "PU2",
        "PU3",
        "PU4",
        "PU7",
        "PU8",
        "PU9",
        "PU10",
        "PU11",
        "PU12",
        "PU13",
        "PU14",
        "PU15",
        "PU16",
        "PU17",
        "PU20",
        "PU25",
        "PU26",
        "PU29",
        "PU34",
        "PU39",
        "PU40",
        "PU42",
        "PU43",
        "PU44",
        "PU53",
        "PU63",
        "STAFF",
        "PU18",
        "PU19",
        "PU21",
        "PU22",
        "PU23",
        "PU24",
        "PU27",
        "PU28",
        "PU30",
        "PU31",
        "PU32",
        "PU33",
        "PU35",
        "PU36",
        "PU37",
        "PU38",
        "PU41",
        "PU48",
        "PU50",
        "PU51",
        "PU52",
        "PU60",
        "PU61",
        "PU64",
        "PU72",
        "PU73",
        "PU74",
        "PU75",
        "PU99",
        "NONSTAFF",
        "GROSS",
        "CREDIT",
        "NET",
    ]


def getPHs():
    return [
        "PH11",
        "PH14",
        "PH15",
        "PH16",
        "PH17",
        "PH21",
        "PH22",
        "PH29",
        "PH30",
        "PH31",
        "PH32",
        "PH33",
        "PH36",
        "PH41",
        "PH42",
        "PH51",
        "PH53",
        "PH64",
        "PH65",
        "TOTAL",
        "EBR-IF",
        "EBR-P",
    ]


def getPHsMap():
    return {
        "PH11": {
            "rowRange": list(range(5, 9)),
            "rowMap": ["CAP", "CAP (CH)", "SF", "TOTAL"],
        },
        "PH14": {
            "rowRange": list(range(10, 12)),
            "rowMap": ["CAP", "TOTAL"],
        },
        "PH15": {
            "rowRange": list(range(13, 16)),
            "rowMap": ["CAP", "CAP (RVNL)", "TOTAL"],
        },
        "PH16": {
            "rowRange": list(range(17, 22)),
            "rowMap": ["CAP", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH17": {
            "rowRange": list(range(23, 27)),
            "rowMap": ["CAP", "DRF", "DF", "TOTAL"],
        },
        "PH21": {
            "rowRange": list(range(28, 33)),
            "rowMap": ["CAP", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH22": {
            "rowRange": list(range(34, 36)),
            "rowMap": ["CAP", "TOTAL"],
        },
        "PH29": {
            "rowRange": list(range(37, 40)),
            "rowMap": ["SF", "RRSK", "TOTAL"],
        },
        "PH30": {
            "rowRange": list(range(41, 44)),
            "rowMap": ["SF", "RRSK", "TOTAL"],
        },
        "PH31": {
            "rowRange": list(range(45, 47)),
            "rowMap": ["RRSK", "TOTAL"],
        },
        "PH32": {
            "rowRange": list(range(48, 52)),
            "rowMap": ["CAP", "DRF", "RRSK", "TOTAL"],
        },
        "PH33": {
            "rowRange": list(range(53, 56)),
            "rowMap": ["CAP", "RRSK", "TOTAL"],
        },
        "PH36": {
            "rowRange": list(range(57, 62)),
            "rowMap": ["CAP", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH41": {
            "rowRange": list(range(63, 68)),
            "rowMap": ["CAP", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH42": {
            "rowRange": list(range(69, 74)),
            "rowMap": ["CAP (RVNL)", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH51": {
            "rowRange": list(range(75, 79)),
            "rowMap": ["CAP", "DRF", "DF", "TOTAL"],
        },
        "PH53": {
            "rowRange": list(range(80, 85)),
            "rowMap": ["CAP", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH64": {
            "rowRange": list(range(86, 91)),
            "rowMap": ["CAP", "DRF", "DF", "RRSK", "TOTAL"],
        },
        "PH65": {
            "rowRange": list(range(92, 96)),
            "rowMap": ["CAP", "DF", "RRSK", "TOTAL"],
        },
        "TOTAL": {
            "rowRange": list(range(97, 105)),
            "rowMap": [
                "CAP",
                "CAP (RVNL)",
                "CAP (CH)",
                "DRF",
                "DF",
                "SF",
                "RRSK",
                "TOTAL",
            ],
        },
        "EBR-IF": {
            "rowRange": [106, 108, 110, 112, 114],
            "rowMap": ["PH15", "PH16", "PH33", "PH42", "TOTAL"],
        },
        "EBR-P": {
            "rowRange": [117, 119, 121],
            "rowMap": ["PH30", "PH36", "TOTAL"],
        },
    }
