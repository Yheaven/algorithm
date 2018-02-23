
import re
import time

class NextSecond():

      def next_seconf(self,str):

          s_list=re.findall("\d+",str)

          s="".join(s_list)

          strptime=time.strptime(s,"%Y%m%d%H%M%S")



          timestamp=time.mktime(strptime)


          new_timestamp=timestamp+1

          new_str=time.localtime(new_timestamp)

          dt=time.strftime("%Y-%m-%d %H:%M:%S", new_str)

          dt_list=re.findall("\d+", dt)

          return"%s年%s月%s日%s时%s分%s秒"% (dt_list[0], dt_list[1], dt_list[2], dt_list[3], dt_list[4], dt_list[5])

if __name__=='__main__':

    a=NextSecond()

    print(a.next_seconf("2017年11月09日23时53分59秒"))
    print(time.localtime())
