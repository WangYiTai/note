var testConter=0;
var startTime=Date.now(); 
function date_time(id)
{
        date = new Date;
        year = date.getFullYear();
        month = date.getMonth();
        months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'Jully', 'August', 'September', 'October', 'November', 'December');
        d = date.getDate();
        day = date.getDay();
        days = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');
        h = date.getHours();
        if(h<10)
        {
                h = "0"+h;
        }
        m = date.getMinutes();
        if(m<10)
        {
                m = "0"+m;
        }
        s = date.getSeconds();
        if(s<10)
        {
                s = "0"+s;
        }
		result = '時間顯示-->碼表<br>'
        //result += ''+days[day]+' '+months[month]+' '+d+' '+year+' '+h+':'+m+':'+s+'-->'+(Date.now()-startTime);
        //result += ''+(month+1)+' '+d+' '+year+' '+h+':'+m+':'+s+'-->'+(Date.now()-startTime);
		result += ''+(month+1)+' '+d+' '+year+' '+h+':'+m+':'+s+'.'+date.getMilliseconds();

		document.getElementById(id).style.fontSize='48px';
		// Set the text-color
		document.getElementById(id).style.color = "magenta";
		// set the backgroundColor
		//document.body.style.backgroundColor = "black";
		//document.getElementById(id).style.backgroundColor = "#00FFFF";
		
		//document.body.style.backgroundImage = "url('SW_Fuminori+Hirayama.JPG')";
		//document.body.style.backgroundImage = "url('giphy.gif')";
		//document.body.style.backgroundRepeat = "repeat"; // "repeat|repeat-x|repeat-y|no-repeat|initial|inherit"
		
		document.body.style.background = "#000000 url('giphy.gif') no-repeat right top";
		
        document.getElementById(id).innerHTML = result;
		testConter++;
		// 設定更新時間
        setTimeout('date_time("'+id+'");','10');
        return true;
}
