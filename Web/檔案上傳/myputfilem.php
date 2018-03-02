<HTML>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>多檔案上傳</title>
</head>
<BODY><H3>上傳多檔案相關資訊：<HR></H3>

<?
for ( $I=0; $I < (count($_FILES["upfile"])-2); $I++ ) 
{
   if ( $_FILES["upfile"]["name"][$I] <> "" ) 
     {
      echo "<BLOCKQUOTE>";
      echo "檔案名稱：" . $_FILES["upfile"]["name"][$I] . "<BR>";
      echo "檔案大小：" . $_FILES["upfile"]["size"][$I] . "<BR>";
      echo "檔案類型：" . $_FILES["upfile"]["type"][$I] . "<BR>";
      echo "暫存檔名：" . $_FILES["upfile"]["tmp_name"][$I] . "<BR>";
     //檢驗檔案大小是否大於0 
     if ( $_FILES["upfile"]["size"][$I] <= 0) 
      {
         echo "上傳檔案錯誤!您傳送的是空檔案!!";
         echo "</BLOCKQUOTE>";
      }
     //檢驗檔案體積是否過大
     else if ( $_FILES["upfile"]["size"][$I] > 50000) 
      {
         echo "上傳檔案錯誤!您傳送的檔案大於50k!!";
         echo "</BLOCKQUOTE>";
      }
     else
      {
        move_uploaded_file($_FILES["upfile"]["tmp_name"][$I], "file\\" . $_FILES["upfile"]["name"][$I]);
         echo "您所上傳的檔案已儲存為 " . $_FILES["upfile"]["name"][$I];
        echo "</BLOCKQUOTE>";
      } 
     }
}
?>

<HR></BODY></HTML>