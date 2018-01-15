// javac  -encoding utf8 VectorApp
// java VectorApp
import java.util.Vector;
import java.lang.*;
import java.util.Enumeration;
public class VectorApp
{
	public static void main(String args[])
	{
		Vector v1 = new Vector();
		Integer integer1= new Integer(1);
		//加入為字串物件
		v1.addElement("one");
		//加入的為integer的對象
		v1.addElement(integer1);
		v1.addElement(integer1);
		v1.addElement("two");
		v1.addElement(new Integer(2));
		v1.addElement(integer1);
		v1.addElement(integer1);
		//轉為字串並列印
		System.out.println("The Vector v1 is:\n\t"+v1);
		//向指定位置插入新對象
		v1.insertElementAt("three",2);
		v1.insertElementAt(new Float(3.9),3);
		System.out.println("The Vector v1(used method insertElementAt()is:\n\t)"+v1);
		//將指定位置的物件設置為新的物件
		//指定位置後的物件依次往後順延
		v1.setElementAt("four",2);
		System.out.println("The vector v1 cused method setElmentAt()is:\n\t"+v1);
		v1.removeElement(integer1);
		//從向量物件v1中刪除物件integer1
		//由於存在多個integer1,所以從頭開始。
		//找刪除找到的第一個integer1.
		Enumeration _enum = v1.elements();
		System.out.println("The vector v1 (used method removeElememt()is");
		while(_enum.hasMoreElements())
		System.out.println(_enum.nextElement()+"");
		System.out.println();
		//使用枚舉類(Enumeration)的方法取得向量物件的每個元素。
		System.out.println("The position of Object1(top-to-botton):"+v1.indexOf(integer1));
		System.out.println("The position of Object1(tottom-to-top):"+v1.lastIndexOf(integer1));
		//按不同的方向查找物件integer1所處的位置
		v1.setSize(4);
		System.out.println("The new Vector(resized the vector)is:"+v1);
		//重新設置v1的大小，多餘的元素被拋棄
	}
}
