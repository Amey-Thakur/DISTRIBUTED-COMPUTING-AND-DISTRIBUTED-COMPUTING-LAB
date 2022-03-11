import java.util.*;
public class LoadBalancing {
public static int l1;
public static int l2;
public static int n;
public static int r1;
public static void main(String[] args) {
r1=0;
Scanner sc=new Scanner(System.in);
System.out.println("we assume two processor. ");
System.out.println("Enter the limit of processor one: ");
l1=sc.nextInt();
System.out.println("Enter the limit of processor two: ");
l2=sc.nextInt();
System.out.println("Enter the number of processes: ");
n=sc.nextInt();
n=n+r1;
Runnable r = new Runnable1();
Thread t = new Thread(r);
Runnable r2 = new Runnable2();
Thread t2 = new Thread(r2);
t.start();
t2.start();
}
}
class Runnable1 implements Runnable{
public void run(){
System.out.println();
int limit1,total1,rem1;
limit1=LoadBalancing.l1;
total1=LoadBalancing.n;
rem1=LoadBalancing.r1;
System.out.println("processor 1 (limit="+limit1+"):");
if(total1==0)
{
System.out.println("No processes are remaining");
}else
{
if(limit1>total1)
{
System.out.println("Underloaded processor");
System.out.println(total1+" processes are executed.");
}
else if(limit1==total1)
{
System.out.println("Normal processor");
System.out.println(total1+" processes are executed.");
System.out.println("No need to forward any process to next processor.");
}
else if(limit1<total1)
{
System.out.println("Overloaded processor");
System.out.println(limit1+" processes are executed.");
rem1=total1-limit1;
System.out.println(+rem1+ " will be forwarded to next processor");
}
}
LoadBalancing.r1=rem1;
}
}
class Runnable2 implements Runnable{
public void run(){
try{Thread.sleep(5000);}catch(InterruptedException e){System.out.println(e);}
System.out.println();
int limit2,total2,rem2,limitp1;
limit2=LoadBalancing.l2;
total2=LoadBalancing.n;
rem2=LoadBalancing.r1;
limitp1=LoadBalancing.l1;
System.out.println("processor 2 (limit="+limit2+"):");
if(rem2==0)
{
System.out.println("No processes are remaining");
}else
{
if(limit2>rem2)
{
System.out.println("Underloaded processor");
System.out.println(rem2+" processes are executed.");
}
else if(limit2==rem2)
{
System.out.println("Normal processor");
System.out.println(rem2+" processes are executed.");
System.out.println("No need to forward any process to next processor.");
}
else if(limit2<rem2)
{
System.out.println("Overloaded processor");
System.out.println(limit2+" processes are executed.");
rem2=total2-(limitp1+limit2);
System.out.println(+rem2+ " will be forwarded to next processor");
}
}
}
}
