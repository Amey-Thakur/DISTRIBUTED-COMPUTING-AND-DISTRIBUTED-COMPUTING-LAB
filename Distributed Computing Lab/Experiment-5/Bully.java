import java.util.*;
import java.util.*;
class Bully
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of processes(starting with 0): ");
        int p;
        p=sc.nextInt();
        int a[]=new int[p+1];
        System.out.println("Enter the process number which fails:  ");
        int f;
        f=sc.nextInt();
        int i;
        for(i=0;i<=p;i++)
        {
            if (i!=f)
            {
                a[i]=1;
            }
            else
            {
                a[i]=0;
            }
        }
        System.out.println("Enter the process which starts election: ");
        int e;
        e=sc.nextInt();
               
        while(e<=p)
        {
            if(e==f)
            {
                e=e+1;
                continue;
            }
                 
            for(i=0;i<=p;i++)
            {

                if(e<i  && (e!=f || e>f))
                {
                    System.out.println("Election message is sent from "+e+ "to" +i);
                }
            }
            e=e+1;
            for(i=0;i<=p;i++)
            {
                if((e<i)&&(i!=f))
                {
                    System.out.println("OK message is sent from "+i+"to"+e);
                }
            }
        }
        System.out.println((e-2)+" is the coordinator");
    }
}