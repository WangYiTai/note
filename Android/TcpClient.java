package tw.com.icm.ble_tvs_demo;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class TcpClient extends Thread
{
	private Socket m_socket;//和伺服器端進行連線
	private String host = null;
	private int port = 0;
	//傳送資料到Server端
	private static DataOutputStream dos = null;
	//傳送資料到Server端
	private static DataInputStream dis = null;

	public TcpClient(String ip, int port)
	{
		this.host = ip;
		this.port = port;
	}
	public void Send(byte[] data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.write(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(byte[] data, int offset, int length)
	{
		if (this.m_socket != null) {
			try {
				this.dos.write(data, offset, length);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(Double data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeDouble(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}

	public void Send(int data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeInt(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(float data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeFloat(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(long data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeLong(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(short data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeShort(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(String data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeBytes(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	public void Send(byte data)
	{
		if (this.m_socket != null) {
			try {
				this.dos.writeByte(data);
			} catch (IOException e) {
				connect();
				//e.printStackTrace();
			}
		}
	}
	
	public void connect()
	{
		try
		{
			m_socket = new Socket(host, port);
			if (m_socket != null)//連線成功才繼續往下執行
			{

				//由於Server端使用 PrintStream 和 BufferedReader 來接收和寄送訊息，所以Client端也要相同
				//傳送資料到Server端
				dos = new DataOutputStream(m_socket.getOutputStream());

				//接收Server端資料
				dis = new DataInputStream(m_socket.getInputStream());
//				while(m_socket.isConnected())
//				{
//					for(int i=0;i<21;i++)
//						System.out.printf("%02X ", dis.readByte());
//					System.out.printf("\n");
//				}
			}
		}
		catch (IOException e)
		{
			System.out.println(e.getMessage());
		}
	}
	@Override
	public void run()
	{
		connect();

	}
}
