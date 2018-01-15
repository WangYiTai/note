## JAVA筆記-wait()、notify()、notifyAll() 執行緒間的等待與喚醒機制的互動 ##
/*
## 必須撰寫在synchronized的區塊內，
## 當wait()被呼叫時，則會釋放所有的鎖，
## 並寫在try-catch(InterruptedException e)內，
## 
## 1. void wait()
## 讓執行緒進入等待狀態
## 2. void notify()
## 喚醒一個等待中的執行緒，若有多個執行緒，則由JVM決定
## 3. void notifyAll()
## 喚醒所有等待中的執行緒
## 
## 注意：考慮在複雜程式上的邏輯正確，在執行緒交互呼叫wait()和notify()時，
## 可能先配合滿足的條件再呼叫函式，例如設計前置布林值或計數器來作為呼叫的條件
##
## 參考網址: http://jhengjyun.blogspot.tw/2011/04/java-waitnotifynotifyall.html
##
*/
import static java.lang.System.out;
public class Ex_WaitNotify {
  public static void main(String[] args) {
    One one = new One();
    one.start();
    synchronized(one) { // 主執行緒取得one的鎖
      String tName = Thread.currentThread().getName();
      out.print("one 進入 wait pool ");
      out.println("(" + tName + ")");
      try {
        one.wait();
      } catch (InterruptedException e) {}
      out.print("one 離開 wait pool ");
      out.println("(" + tName + ")");
    }
  }
}

class One extends Thread {
  public void run() {
    synchronized (this) {
      String tName = Thread.currentThread().getName();
      out.print("呼叫 notify() ");
      out.println("(" + tName + ")");
      notify();
      out.print("notify() 呼叫完畢! ");
      out.println("(" + tName + ")");
    }
  }
}
