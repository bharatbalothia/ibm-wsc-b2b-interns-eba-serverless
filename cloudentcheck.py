from cloudant.client import Cloudant

client = Cloudant("e06b4c3d-78c6-4f21-8bb3-297e658dc8b1-bluemix", "4299f4e82a5b36181a52abd82d9d74bd5bf3f77a350d5db2daf9b30882df8cb8",
                  url="https://e06b4c3d-78c6-4f21-8bb3-297e658dc8b1-bluemix:4299f4e82a5b36181a52abd82d9d74bd5bf3f77a350d5db2daf9b30882df8cb8@e06b4c3d-78c6-4f21-8bb3-297e658dc8b1-bluemix.cloudantnosqldb.appdomain.cloud", connect='true')

db = client['transactions']

dataDump = [
      {"isa": "ISA0000124155559874ZZI1207",  "name": "walgreens",       "type": "pharmacy"},
      {"isa": "ISA0000124345350274ZZI0323",  "name": "cvs",             "type": "pharmacy"},
      {"isa": "ISA0000123829384948ZZI0213",  "name": "rite aid",        "type": "pharmacy"},
      {"isa": "ISA0000126109292296ZZI0637",  "name": "asd healthcare",  "type": "distributor"},
      {"isa": "ISA0000128182992837ZZI0293",  "name": "besse medical",   "type": "distributor"},
      {"isa": "ISA0000144182938388ZZI0374",  "name": "cubbix",          "type": "manufacturer"},
      {"isa": "ISA0000129163309292ZZI0275",  "name": "ics",             "type": "manufacturer"},
      {"isa": "ISA0000129162209123ZZI0872",  "name": "innomar",         "type": "pharmacy"},
      {"isa": "ISA0000125559299383ZZI0192",  "name": "pharmedium",      "type": "provider"},
      {"isa": "ISA0000126452883834ZZI0394",  "name": "xcenda",          "type": "consultant"},
      {"isa": "ISA0000127465535363ZZI1542",  "name": "michigan health", "type": "pharmacy"},
      {"isa": "ISA0000122738374833ZZI0332",  "name": "dollar",          "type": "pharmacy"},
      {"isa": "ISA0000122635820384ZZI0090",  "name": "ace",             "type": "pharmacy"},
      {"isa": "ISA0000122636283847ZZI0120",  "name": "adrojan",         "type": "distributor"},
      {"isa": "ISA0000121929382922ZZI0469",  "name": "eamon",           "type": "distributor"},
      {"isa": "ISA0000122921921922ZZI0847",  "name": "earleen",         "type": "manufacturer"},
      {"isa": "ISA0000124653933462ZZI0473",  "name": "tacitus",         "type": "manufacturer"},
      {"isa": "ISA0000122347364922ZZI0482",  "name": "tahoe",           "type": "pharmacy"},
      {"isa": "ISA0000121844736362ZZI0283",  "name": "jacinto",         "type": "provider"},
      {"isa": "ISA0000123373382823ZZI0923",  "name": "jafar",           "type": "consultant"},
      {"isa": "ISA0000122727363443ZZI0355",  "name": "parsons systems", "type": "pharmacy"},
      {"isa": "ISA0000123168862713ZZI0637",  "name": "ece healthcare",  "type": "distributor"},
      {"isa": "ISA0000121232131828ZZI0409",  "name": "barlow medical",  "type": "distributor"},
      {"isa": "ISA0000123839484857ZZI0536",  "name": "lagina",          "type": "manufacturer"},
      {"isa": "ISA0000121722636334ZZI0839",  "name": "sfg",             "type": "manufacturer"},
      {"isa": "ISA0000012554732645ZZI0092",  "name": "taras medical",   "type": "pharmacy"},
      {"isa": "ISA0000121233944942ZZI0288",  "name": "ebs pharmacy",    "type": "provider"},
      {"isa": "ISA0000128278383747ZZI0872",  "name": "teague",          "type": "consultant"}
]

datadump1 = [

  {"parentID": "a6LxJKvgSiOB2emh", "ID": "WsX1DQOuc5cynj2a", "type": "purchase", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-22T01:20:00+00:00" },
  {"parentID": "a6LxJKvgSiOB2emh", "ID": "LtbMNaPRvaVuDerl", "type": "acknowledgement", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-22T01:45:00+00:00" },
  
  {"parentID": "BdzKwC1EoO7gOHrT", "ID": "5RUMkO4S4WuTDkvR", "type": "purchase", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-11T01:20:00+00:00" },
  {"parentID": "BdzKwC1EoO7gOHrT", "ID": "Ofhgte3bQ2z6ovYb", "type": "acknowledgement", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-11T01:25:00+00:00" },
  
  {"parentID": "fEBNgZ8Q2sUqQKmI", "ID": "vjwTYCqzYfkchEZA", "type": "purchase", "tradingPartnerID": "ISA0000123829384948ZZI0213", "success": 'false', "code": "bad data", "timestamp": "2019-04-12T00:40:00+00:00" },
  
  {"parentID": "MfKp9GZuZQaHWHWY", "ID": "DSFZQV6bByncOwEo", "type": "purchase", "tradingPartnerID": "ISA0000126109292296ZZI0637", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-19T01:20:00+00:00" },
  
  {"parentID": "mr296RemYNau48w3", "ID": "AGjFLp5kVcu0QF0H", "type": "cancelation", "tradingPartnerID": "ISA0000128182992837ZZI0293", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-19T01:41:00+00:00" },

  {"parentID": "VwTSlR0e4eLtecE2", "ID": "FrRGOm1VMmuJgcqd", "type": "purchase", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-20T01:42:00+00:00" },
  {"parentID": "VwTSlR0e4eLtecE2", "ID": "px43ZEB288dD4Jur", "type": "acknowledgement", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp":"2019-04-20T01:30:00+00:00" },
  {"parentID": "VwTSlR0e4eLtecE2", "ID": "px43ZEB288dD4Jur", "type": "cancelation", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-20T01:50:00+00:00" },
  
  {"parentID": "b6fcJSvfSiOB2emh", "ID": "WsX1DQOuc5cynj2a", "type": "purchase", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-02T01:20:00+00:00" },
  {"parentID": "b6fcJSvfSiOB2emh", "ID": "LtbMNaPRvaVuDerl", "type": "acknowledgement", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-02T01:23:00+00:00" },
  
  {"parentID": "x1m2Fol22bedgAoo", "ID": "zg7FqjapMUVl560E", "type": "purchase", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-12T01:00:00+00:00" },
  {"parentID": "x1m2Fol22bedgAoo", "ID": "SRGcID7HHdd7kzol", "type": "acknowledgement", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-12T01:35:00+00:00" },
  
  {"parentID": "cq9i37NZ95ciQcm9", "ID": "PBYGhGnHBhCcHvZg", "type": "purchase", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-13T01:20:00+00:00" },
  {"parentID": "cq9i37NZ95ciQcm9", "ID": "Ofhgte3bQ2z6ovYb", "type": "acknowledgement", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-13T01:30:00+00:00" },
  
  {"parentID": "AJfxnJz0dcV0xxuI", "ID": "S6hABxZiFMgGogpn", "type": "purchase", "tradingPartnerID": "ISA0000123829384948ZZI0213", "success": 'false', "code": "bad data", "timestamp": "2019-04-14T00:40:00+00:00" },
  
  {"parentID": "9Tq6Yj1LipTikSDR", "ID": "8hwHuFmfM7oJC1VS", "type": "purchase", "tradingPartnerID": "ISA0000126109292296ZZI0637", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-16T01:20:00+00:00" },
  
  {"parentID": "mQmtHmfauijMXGXq", "ID": "oGL61oc80KLVdFj1", "type": "cancelation", "tradingPartnerID": "ISA0000128182992837ZZI0293", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-18T01:41:00+00:00" },

  {"parentID": "ia9d91vdP6h3qvaO", "ID": "jcLj3f7fGdpPhQSG", "type": "purchase", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-18T01:42:00+00:00" },
  {"parentID": "ia9d91vdP6h3qvaO", "ID": "BcrtOgi4cPPdBCbi", "type": "acknowledgement", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp":"2019-04-18T01:30:00+00:00" },
  {"parentID": "ia9d91vdP6h3qvaO", "ID": "Na4i8pwbaWpZDnhQ", "type": "cancelation", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-18T02:05:00+00:00" },
  
  {"parentID": "sUVZ3rdRYNGdcdSW", "ID": "ZgW9y6cnruH61p57", "type": "purchase", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-04T01:40:00+00:00" },
  {"parentID": "sUVZ3rdRYNGdcdSW", "ID": "0jJxJriyEfvpfQLG", "type": "acknowledgement", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-04T01:43:00+00:00" },
  
  
  
  {"parentID": "szh9XdH63JlNWi67", "ID": "h3SDmnnZqzayhmL6", "type": "purchase", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-22T01:22:00+00:00" },
  {"parentID": "szh9XdH63JlNWi67", "ID": "3KCurtYLjN9pgVRw", "type": "acknowledgement", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-22T01:24:00+00:00" },
  
  {"parentID": "DbzBnqaiK0aGoEGu", "ID": "zaRXMmH2Sy6Prm1W", "type": "purchase", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-11T01:10:00+00:00" },
  {"parentID": "DbzBnqaiK0aGoEGu", "ID": "wMn6pNLfftMJgXFQ", "type": "acknowledgement", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-11T01:25:00+00:00" },
  
  {"parentID": "S6o0SNStkFFRVQYw", "ID": "MrArhAEBxTyB6wJU", "type": "purchase", "tradingPartnerID": "ISA0000123829384948ZZI0213", "success": 'false', "code": "bad data", "timestamp": "2019-04-12T00:40:00+00:00" },
  
  {"parentID": "GXbfO5Cgsmk5vujr", "ID": "cMz7Nmy4GPkUMWsO", "type": "purchase", "tradingPartnerID": "ISA0000126109292296ZZI0637", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-19T01:20:00+00:00" },
  
  {"parentID": "oxo9yajKcOVHXfYq", "ID": "F3OJFmm7VhB55ujs", "type": "cancelation", "tradingPartnerID": "ISA0000128182992837ZZI0293", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-19T01:41:00+00:00" },

  {"parentID": "zo21rHsQB8pKLGof", "ID": "USczHIv9R3jg9Hfr", "type": "purchase", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-20T01:42:00+00:00" },
  {"parentID": "zo21rHsQB8pKLGof", "ID": "NBg2Ns5GAAwaIpxv", "type": "acknowledgement", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp":"2019-04-20T01:30:00+00:00" },
  {"parentID": "zo21rHsQB8pKLGof", "ID": "LKhzyUraZCIT3fx8", "type": "cancelation", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-20T01:45:00+00:00" },
  
  {"parentID": "o2NPTjCO0UpWjN8x", "ID": "QI2DkTmKpwyhhES0", "type": "purchase", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-02T01:00:00+00:00" },
  {"parentID": "o2NPTjCO0UpWjN8x", "ID": "LlX5WA7fJZGucYan", "type": "acknowledgement", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-02T01:55:00+00:00" },
  
  {"parentID": "c1Zhu2yWMN3MPKto", "ID": "fa9B0MlUuaisKx5i", "type": "purchase", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-12T01:00:00+00:00" },
  {"parentID": "c1Zhu2yWMN3MPKto", "ID": "AjCzeaR0DgzRfX5u", "type": "acknowledgement", "tradingPartnerID": "ISA0000124155559874ZZI1207", "success": 'true', "code": "", "timestamp": "2019-04-12T01:55:00+00:00" },
  
  {"parentID": "cqFD6gP86xGHtGlf", "ID": "bue0X66fjmg76kUx", "type": "purchase", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-13T01:22:00+00:00" },
  {"parentID": "cqFD6gP86xGHtGlf", "ID": "8dAO1QN9KNRbyvct", "type": "acknowledgement", "tradingPartnerID": "ISA0000124345350274ZZI0323", "success": 'true', "code": "", "timestamp": "2019-04-13T01:24:00+00:00" },
  
  {"parentID": "C3pZlhJ56EX24dC7", "ID": "9nSOWN8VNJPOtguJ", "type": "purchase", "tradingPartnerID": "ISA0000123829384948ZZI0213", "success": 'false', "code": "bad data", "timestamp": "2019-04-14T00:40:00+00:00" },
  
  {"parentID": "1kj8M4JULfpBSJVR", "ID": "Fi8wyJrS1r7bQAht", "type": "purchase", "tradingPartnerID": "ISA0000126109292296ZZI0637", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-16T01:20:00+00:00" },
  
  {"parentID": "KoOP3lhFFTYKHatU", "ID": "UqknmtBjlglEC7xO", "type": "cancelation", "tradingPartnerID": "ISA0000128182992837ZZI0293", "success": 'false', "code": "invalid product numbers", "timestamp": "2019-04-18T01:41:00+00:00" },

  {"parentID": "tDZ0nDTe2QwUiz52", "ID": "65g63xVCJeN37Vkg", "type": "purchase", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-18T01:42:00+00:00" },
  {"parentID": "tDZ0nDTe2QwUiz52", "ID": "sQPgfdq1BuMU26y1", "type": "acknowledgement", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp":"2019-04-18T01:30:00+00:00" },
  {"parentID": "tDZ0nDTe2QwUiz52", "ID": "nk98kW1HHVbs5aPj", "type": "cancelation", "tradingPartnerID": "ISA0000144182938388ZZI0374", "success": 'true', "code": "", "timestamp": "2019-04-18T01:46:00+00:00" },
  
  {"parentID": "9hx6yakFb7aXz3Hf", "ID": "UtrKQgxWu7nTrtVt", "type": "purchase", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-04T01:40:00+00:00" },
  {"parentID": "9hx6yakFb7aXz3Hf", "ID": "X6DoPr8hiBEx6P5M", "type": "acknowledgement", "tradingPartnerID": "ISA0000129163309292ZZI0275", "success": 'true', "code": "", "timestamp": "2019-04-04T01:56:00+00:00" }
  
]

for data in datadump1:
    my_document = db.create_document(data)
    # Check that the document exists in the database
    if my_document.exists():
        print('SUCCESS!!')

'''


for data in db:
    print(data)
'''    
client.disconnect()
