from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#"database"
users = {
    "thuha": {
        "password": "0105",
        "message": "Chị iu thu hà nhìu lắm, gà chip mi nhon của chị. Chúc cưng sẽ luôn khỏe mạnh, iu đời nhé (iu chị nữa nha) <3. Chị chưa bao giờ nghĩ là hai chị em mình hợp nhau luôn, tại ấn tượng của chị với em là đi trễ...hehe nhưng mà mấy tháng làm việc cùng nhau thấy bé cũng dễ thương, zui zẻ keke, hong làm nội dung chung với em, nhưng mong là em đã có một trải nghiệm thật đẹp với Pidi, và TNTT nha! Love moazzzzie. P/s nhỏ: Quà sinh nhật em chị sẽ hong quên âu nè."
    },
    "thanhquynhdaangel": {
        "password": "2601",
        "message": "Thanh Quỳnh, ck iu, thiên thần của em ơi! Lời đầu tiên, choa phép chóo xin lỗi TQ nhiều lắm, tại em cũng còn bay, còn xa cách với team vào giai đoạn cuối á. Nhưng mà ck luôn hiểu cho em TT, thương và cảm ơn ck nhiều lắm. Flashback lại từ những ngày đầu Quỳnh nhắn hỏi em, rùi phỏng vấn tụi nhỏ, xong tới ngày cuối cùng onsite, em thấy wow, sao mà nhanh quá zị. TQ của em đã có 1 last dance rực rỡ ở nhà Đoàn rùi, chúc ck sẽ thành công trên con đường sắp tới nữa nhoaa <3"
    },
    "cktong": {
        "password": "2302",
        "message": "Iu ck tống, Chúc ck luôn rạng rỡ, thành công và có thêm nhiều thành quả tuyệt vời nữa trong tương lai!"
    },
    "binhan": {
        "password": "3110",
        "message": "Bình An đúng như tên gọi thì luôn mang lại sự yên bình, nhưng mà đôi lúc c thấy em cx hơi bốc đó nha kkkk. Chúc em sẽ mãi giữ được tâm hồn nhiệt huyết, dám nói, dám làm ấy, gặp được nhiều người tốt và luôn sống thật vui vẻ nhé! Em giỏi lắm rùiii"
    },
    "mquan": {
        "password": "1309",
        "message": "Minh Quân ơi! Chị 'cảm ơn' vì những khoảnh khắc dễ thương, hài hước của em nha, hình dìm chị cũng dữ dội ghê á. Chúc em luôn là chính mình và thật thành công với những gì em theo đuổi nhă! You did great! Em đã làm được nhiều rùi nèe"
    },
    "ngocminh": {
        "password": "2509",
        "message": "Chúc ngọc minh bé iu đi học chung vs chị sẽ lun điểm cao hè hè, bớt cúp học lại, hehe. Chúc em sẽ thật khỏe mạnh và luôn đạt được kết quả tốt nha! Iu em."
    },
    "lanh": {
        "password": "2402",
        "message": "Lanh lanh lanh, chúc lan anh của chị sẽ thật thành công hehe, thích cái cách em luôn bình tĩnh xử lý mọi task chị giao <3, cố lên nhe, proud of u so muchhh. Em học nhanh và cố gắng nhiều lắm, chị biết hết nè, bé cưng của chị keke, love ur effort"
    },
    "anhtan": {
        "password": "0902",
        "message": "Anh Tân thân thiện ơi! Chúc em luôn đạt được những điều em mong muốn và tiếp tục truyền cảm hứng tích cực đến mọi người xung quanh nha! Chị hong tiếp xúc nhiều với em, nhưng mà em cũng giỏi lém nè, cảm ơn em vì bông hoa nha kakak <3"
    },
    "minhthu": {
        "password": "0206",
        "message": "Chúc minh thư sẽ luôn đạt được ước mơ, và thành công trên con đường mình theo đuổi nha! Cảm on8 em vì đã lắng nghe chị và tiến bộ từng ngày, chị thấy rõ được điều đó nè, hong sao đâu. Wish u the best <3"
    },
    "thanhnhi": {
        "password": "2911",
        "message": "thanh nhii dịu dàng ơi! Chị rất vui vì đã gặp em trong hành trình này. Mong em luôn giữ được sự nhiệt huyết và trái tim ấm áp của mình nhaaa. Cao v mà ko thi FTUCharm uổng quá đi kkkkk, lớn làm celeb idol đừng quên chị hehe <3"
    }
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if username in users and users[username]["password"] == password:
            return redirect(url_for("message", username=username))
        else:
            return render_template("login.html", error="Sai tên hoặc mật khẩu rùi!")

    return render_template("login.html")

@app.route("/message/<username>")
def message(username):
    if username in users:
        return render_template("message.html", username=username, message=users[username]["message"])
    return "Người dùng không tồn tại!", 404

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
