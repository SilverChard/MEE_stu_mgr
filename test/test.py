# coding=utf-8
import json

# 01 23 45
# 23 07 09
c_dict = {}
dis_dict = {}
city_dict = {}
province_dict = {}
c_dict['86'] = {}
fl = open('dis.txt')
data = fl.readline()
while data:
    data = data.split(' ')
    dis_id = data[0]
    dis_name = "%s" % str(data[1][:-1].decode('utf-8'))
    if dis_id == "230700":
        pass
    if dis_id[2] == '0' and dis_id[3] == '0' and dis_id[4] == '0' and dis_id[5] == '0':  # example: 230000 黑龙江
        c_dict['86'].update({"%s" % dis_id: "%s" % dis_name})
    if (dis_id[2] != '0' or dis_id[3] != '0') and dis_id[4] == '0' and dis_id[5] == '0':  # example: 230700 伊春
        if not c_dict.has_key('%s0000' % dis_id[0:2]):
            c_dict['%s0000' % dis_id[0:2]] = {}
        c_dict['%s0000' % dis_id[0:2]].update({"%s" % dis_id: "%s" % dis_name})
    if (dis_id[2] != '0' or dis_id[3] != '0') and (dis_id[4] != '0' or dis_id[5] != '0'):  # example: 230709 金山屯
        if not c_dict.has_key('%s00' % dis_id[0:4]):
            c_dict['%s00' % dis_id[0:4]] = {}
        c_dict['%s00' % dis_id[0:4]].update({"%s" % dis_id: "%s" % dis_name})

    data = fl.readline()



fs = open('dis_res.txt', 'w+')
c_str = json.dumps(c_dict, ensure_ascii=False)
print  c_str
fs.write(c_str)
