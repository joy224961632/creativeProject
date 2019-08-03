var time = $("#time").text();
var tall = $("#text").text();
time = time.substring(0,19);
var detect;
if(tall > 160){
    detect = "大人";
}else{
    detect = "小孩";
}
$("#img").attr("src","Upload.png");
$("title").text("創意賽專題");
$("#text").text(`此人身高:${tall},判斷為${detect}`);
$("#text").removeClass("hidden");
$("#time").text(`上次更新時間:${time}`);
$("#time").removeClass("hidden");