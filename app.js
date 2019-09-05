var time = $("#time").text();
var tall = $("#text").text();
var face = $("#face").text();
console.log(face)
time = time.substring(0, 19);
var detect;
if (tall > 160) {
    detect = "大人";
} else {
    detect = "小孩";
}
$("#img").attr("src", "Upload.png");
$("title").text("創意賽專題");
$("#text").text(`身高:${tall} 公分`);
$("#text").removeClass("hidden");
$("#time").text(`上次更新時間:${time}`);
$("#time").removeClass("hidden");
$("#dectect").text(`他是:${detect}`);
$("h1").text("高中職創意賽");
$("#face").text(`他的表情是:${face}`);