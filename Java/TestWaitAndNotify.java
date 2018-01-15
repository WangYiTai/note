public class TestWaitAndNotify {
    Call call = new Call(false);
    //boolean IsNotifyAll = true;
    boolean IsNotifyAll = false;

    class MaMa extends Thread {
        public MaMa(String name) {
            super(name);
        }

        @Override
        public void run() {
            synchronized(call) {
                try {
                    call.wait(3000);
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
                call.setFlag(true);
                if (IsNotifyAll) {
                    call.notifyAll();
                } else {
                    for (int i = 0; i < 3; i++) {
                        System.out.println("進來一個吧");
                        call.notify();
                        try {
                            call.wait(1000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
    }

    class Customer extends Thread {
        public Customer(String name) {
            super(name);
        }

        @Override
        public void run() {
            synchronized(call) {
                while (!call.isFlag()) {
                    System.out.println(Thread.currentThread().getName() + "等待王媽媽的呼喚");
                    try {
                        call.wait();
                    } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }
                }
                System.out.println(Thread.currentThread().getName() + "進入小姐的房間");
            }
        }
    }

    public static void main(String[] args) {
        TestWaitAndNotify test = new TestWaitAndNotify();
        MaMa teacher = test.new MaMa("王媽媽");
        Customer stu1 = test.new Customer("小米");
        Customer stu2 = test.new Customer("小百");
        Customer stu3 = test.new Customer("小阿");
        teacher.start();
        stu1.start();
        stu2.start();
        stu3.start();

    }
}

class Call {
    private boolean flag = false;

    public Call(boolean flag) {
        this.flag = flag;
    }

    public boolean isFlag() {
        return flag;
    }

    public void setFlag(boolean flag) {
        this.flag = flag;
    }
}