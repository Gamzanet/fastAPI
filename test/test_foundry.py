import requests
import json
import time

payload_1 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x693153d5d512f343ff89CDdBBf18019c226241D0"
    },
    "mode" : 2
  }
})#  not implement hook

payload_2 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x7e06d9b96178ab9e3d0d27f84f29476e42057ff0",
    },
    "mode" : 2
  }
})# storage oob hook
# 
payload_3 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x346b5B6a99a695cdc4820958B846Ab599c693FF0"
    },
    "mode" : 2
  }
}) ## oog
payload_4 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x693153d5d512f343ff89CDdBBf18019c226241D0"
    },
    "mode" : 2
  }
}) ## oog
payload_5 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x3c712B5E5B4a7ee97E4e3F2330bFb435050a4800"
    },
    "mode" : 2
  }
}) ## kenny's oog
payload_6 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x7e06d9b96178ab9e3d0d27f84f29476e42057ff0"
    },
    "mode" : 2
  }
})#  unichain for-loop hook

payload_7 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xce12A4E8980a70B0f4Bf16d89dD734dDb507Cac0"
    },
    "mode" : 2
  }
})#  only by pool manager clear

payload_8 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x697c70532f481D823ef3606b77EC94396Bfd8aC0"
    },
    "mode" : 2
  }
})#  time out hook
#
url = "http://localhost:8000/api/tasks"

headers = {
    'Content-Type': 'application/json'
}

_payload_1 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x89e598609ada63375b9e3188d45c54f9f21bfff0"
    },
    "mode" : 2
  }#
})# all hook - complate

_payload_2 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x7d61d057dD982b8B0A05a5871C7d40f8b96dd040"
    },
    "mode" : 2
  }#
})# takeprofit - complate


_payload_3 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xb15ce080C38508a50a46c827c6D596da1e03a080"
    },
    "mode" : 2
  }#
})# double init

_payload_3 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xb15ce080C38508a50a46c827c6D596da1e03a080"
    },
    "mode" : 2
  }#
})# double init
_payload_4 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x15F3F147eB0278b46363529083751363Be248c00"
    },
    "mode" : 2
  }#
})# proxy hook
_payload_5 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xd7b5397f95fA038e78dae2FD5956f11805bd8aC0"
    },
    "mode" : 2
  }#
})# 30 days hook
_payload_6 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xF20Ac4669fc2bbAC775B46875E22Ba851bF64AC0"
    },
    "mode" : 2
  }#
})# 304 days hook
_payload_7 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xEB0E9255aaB63951464f8adF268f676575E92000"
    },
    "mode" : 2
  }#
})# init err hook


_payload_8 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 8388608,
		"tickSpacing": 60,
		"hooks": "0xb481719eFaE432b5268acC4166A95Dc68d928Ac0"
    },
    "mode" : 2
  }#
})# dynamic fee
# 0x9a52b4ed222B225372b485AA27f66E0bD0D53FF0

_payload_9 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x356dc5a1783fA308673eE2C6EbfcfaA02d1bfFF0"
    },
    "mode" : 2
  }#
})# init double hook
_payload_10 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xb481719eFaE432b5268acC4166A95Dc68d928Ac0"
    },
    "mode" : 2
  }#
})# time 
_payload_10 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0xf83d095f1a2c1A79acA5Ba499a81d18023e8bFf0"
    },
    "mode" : 2
  }#
})# real loop 
##
_payload_11 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x6e49020Cc72cB9CDB4647dbA3f62Fbb7b4Ae6080"
    },
    "mode" : 2
  }# double init unable hook
})
_payload_12 = json.dumps({
  "data": {
    "Poolkey": {
		"currency0": "0x6aD83000194DFCf9a0869091B2Ea7D121033163E",
		"currency1": "0xe61398b1Cb0FBED8268808A983Ad71ECFE2e1Ee9",
		"fee": 0,
		"tickSpacing": 60,
		"hooks": "0x15F3F147eB0278b46363529083751363Be248c00"
    },
    "mode" : 2
  }#proxy hook
})
print("double-init hook")
port = 8000
host = "http://localhost:{}/api".format(port)
tasks = "/tasks"
noti = "/noti/{}/{}/{}/"
result = "/result/{}"

res = requests.post(host+tasks, headers = headers, data = _payload_6)
t = ["minimum", "time", "hookcmp", "price", "chkPM", "timestep", "doubleInit", "proxy"]
print(res.text)
d = json.loads(res.text)['info']#['tasks']
print("timehash : {}".format(d["timeHash"]))
print("hooks : {}".format(d["hooks"]))
print("{}{}".format(host, noti.format(d["timeHash"], d["hooks"], 2, 0)))
print("{}{}".format(host, noti.format(d["timeHash"], d["hooks"], 2, 1)))
print("{}{}".format(host, noti.format(d["timeHash"], d["hooks"], 2, 2)))
for i in range(len(d['tasks'])):
  print("=======================")
  print("test : {}".format(t[i]))
  print("{}{}".format(host, result.format(d['tasks'][i]['id'] ) ) )
  print("=======================")

