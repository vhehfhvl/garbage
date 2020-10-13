import GPUtil
from threading import Thread
import time
import logging
import datetime

def log_chat(gpu_util, question, answer, generation_time):
    GPUs = GPUtil.getGPUs()
    for GPU in GPUs:
        print('sep')
        logging.basicConfig(filename='/KoGPT2chatbot/log/chat/{}_chat.log'.format(datetime.datetime.now().strftime('%Y-%m-%d')), level=logging.DEBUG)
        print('sep2')
        print('/KoGPT2chatbot/log/chat/{}_chat.log'.format(datetime.datetime.now().strftime('%Y-%m-%d')))
        logging.debug('{}, {}, used_memory={}/{}, max_utilization={}, q={}, a={}, generation_time={}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), GPU.name, GPU.memoryUsed, GPU.memoryTotal, gpu_util, question, answer, generation_time))
