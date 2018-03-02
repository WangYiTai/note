# -*- coding:utf-8 -*-
#!/usr/local/bin/python

import os
from datetime import datetime
import shutil
import sys

#�P�_�ɮ׬O�_���Ϥ�
def is_imag(filename):
    return os.path.splitext(filename)[-1] in [".png", ".jpg"]

	#���o�Ϥ��إ߮ɶ�
def get_time(filename):
    timestamp = os.stat(filename).st_mtime
    return datetime.fromtimestamp(timestamp)

#listdir �|�C�X�ؼи�Ƨ����Ҧ��ɮצW��
if len(sys.argv) < 2:
    filenames = os.listdir(".")
else :
    filenames = os.listdir(sys.argv[1])


#���o�Ҧ��Ϥ����ɦW
images = filter(is_imag, filenames)

filenames = images

#�N�ɮר̮ɶ��Ƨ�
#filenames.sort(key=get_time)

last_modified = None
for filename in filenames:
    modified = get_time(sys.argv[1]+"/"+filename)

    #�M�w�y�����A�Y�ק諸����P�e�@���ɮ׬ۦP�ɬy�����[ 1
    if last_modified and last_modified.date() == modified.date():
        num += 1
    else:
        num = 1

    #�̾ڮɶ��M�y�����M�w�ɮ�
    targetname = "{}.jpg".format(modified.strftime("%Y%m%d-%H%M%S"))

    #��W
    shutil.move(sys.argv[1]+"/"+filename, sys.argv[1]+"/"+targetname)

    last_modified = modified