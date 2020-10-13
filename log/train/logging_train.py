import GPUtil,logging,datetime,time
from logging import handlers

def log_train(gpu_memory, gpu_util, start, epoch, batch_size):
  end = time.time() # end time
  LogFormatter = logging.Formatter('%(asctime)s,%(message)s')

  now = datetime.datetime.now()
  nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
  filename = nowDateTime + '_train.log'
  LogHandler = handlers.TimedRotatingFileHandler(filename='./log/train/{}'.format(filename), interval = 1, encoding='utf-8')
  LogHandler.setFormatter(LogFormatter)
  LogHandler.suffix = "%Y%m%d"

  #logger set
  Logger = logging.getLogger()
  Logger.setLevel(logging.DEBUG)
  Logger.addHandler(LogHandler)
  
  #use logger
  gpus = GPUtil.getGPUs()
  contents = str(gpus[0].name) + ", memory_used= " + str(gpu_memory) + "/" + str(gpus[0].memoryTotal) + ", max_utilization= " + str(gpu_util) + ", epoch= " + str(epoch) + ", batch_size= " + str(batch_size) + ", learning_time= " + str(end - start)
  print(contents)
  Logger.debug(contents)
