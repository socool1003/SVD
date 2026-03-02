import turtle
import time


def draw_heart():
    # 1. 设置画布
    window = turtle.Screen()
    window.title("Python Heart for You")
    window.bgcolor("black")  # 背景黑色

    # 2. 设置画笔
    love = turtle.Turtle()
    love.shape("turtle")
    love.color("red")
    love.speed(3)  # 速度：1最慢，10最快
    love.begin_fill()  # 开始填充颜色

    # 3. 开始画心
    # 原理：左转 -> 直走 -> 画半圆 -> 画半圆 -> 直走 -> 回原点
    love.left(140)
    love.forward(180)

    # 画左边的圆弧
    love.circle(-90, 200)

    # 调整方向画右边的圆弧
    # setheading用于设置当前朝向的角度
    love.setheading(60)
    love.circle(-90, 200)

    love.forward(180)
    love.end_fill()  # 结束填充

    # 4. 写字
    love.up()
    love.goto(0, -50)
    love.color("white")
    love.write("Love form AI", align="center", font=("Arial", 20, "bold"))

    # 5. 点击窗口关闭
    window.exitonclick()


if __name__ == "__main__":
    draw_heart()