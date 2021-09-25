import javax.swing.*;  
import java.util.ArrayList;
import java.util.Random;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Color;
import java.awt.Font;
import java.awt.Rectangle;
import java.awt.geom.Rectangle2D;

class DrawRectangle extends JComponent{
    public void paintComponent(Graphics g){
        Graphics2D g2=(Graphics2D) g;
        g2.setPaint(Color.RED);
        Rectangle2D rect=new Rectangle2D.Double(50,50,200,200);
        g2.draw(rect);
        g2.fill(rect);
    }
}

public class Sorter extends JFrame{  
	static int numElements = 10; 
	static int width = 800;
	static int height = 600;
	static ArrayList<Integer> nums = new ArrayList<Integer>();
	static Random rand = new Random();

	public static void newList(){
		for(int i = 0; i <= numElements; i++){
					int randomNum = rand.nextInt(300);
					nums.add(randomNum);
				}
	}
	public static void main(String[] args) {  
		newList();

		// Create J Frame
		JFrame f=new JFrame("Sorting Algorithms"); 
		f.setSize(width,height);
		f.setLayout(null);//using no layout managers  
		f.setVisible(true);//making the frame visible          
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       		
		int arrWidth = width - 50;
		int eachCol = (int) ((arrWidth / nums.size()));
		int xPos = 0;
		for(int j = 1; j <= numElements + 1; j++){
			int i = j-1;
			System.out.println("------");
			System.out.println("arrWidth " +arrWidth);
			System.out.println("eachCol " +eachCol);
			System.out.println(nums.get(j));
			
			int colHeight = nums.get(i);
			
			System.out.println("colHeight "+colHeight);
			
			int tempX = (int) (width/numElements);
			System.out.println("TempX "+tempX);
			if(xPos == 0) {
				xPos = xPos = 10;
			}
			else {
				xPos = xPos + tempX;
			}
			System.out.println("x = "+xPos);
			DrawRectangle rec= new DrawRectangle();
	        //			  x          y    	   W        H
			//rec.setBounds(xPos/2,400-colHeight,eachCol,colHeight);
			rec.setBounds(xPos-10, 400-colHeight,eachCol,colHeight);
			f.add(rec);
			JLabel l = new JLabel();
			l.setText(Integer.toString(nums.get(j)));
			l.setBounds(xPos, 400, 100, 100);
			l.setFont(new Font("Serif", Font.PLAIN, eachCol/3));
			f.add(l);
		}
		
		
	}  
}  
