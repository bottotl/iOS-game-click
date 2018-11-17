# coding: utf-8
import atx
import time

def click_image(d, image):
	FindPoint = d.exists(image)
	if FindPoint:
		p_click(d, FindPoint)
		return FindPoint

def p_click(d, FindPoint):
	dis = d.display
	y = dis.height - FindPoint.pos[0]
	x = FindPoint.pos[1]
	d.click(x, y)

def click(d, x1, y1):
	dis = d.display
	y = dis.height - x1
	x = y1
	d.click(x, y)

def gongji(d):
	print("start gongji")
	while 1:

		if click_image(d, "kaishishouyao.750x1334.png") != None:
			print("kaishishouyao")

		click(d, 398, 1046)
		click(d, 398, 1160)
		click(d, 398, 1260)
		click(d, 58, 1056)
		click(d, 728, 1136)
		click(d, 598, 46)
		if click_image(d, "jixu.750x1334.png") != None:
			print("jixu")
			break
		click(d, 398, 1046)
		click(d, 398, 1160)
		click(d, 398, 1260)
		click(d, 58, 1056)
		click(d, 728, 1136)
		click(d, 598, 46)
	print("end gongji")

def swipe(d, x1, y1, x2, y2):
	dis = d.display
	y11 = dis.height - x1
	x11 = y1

	y22 = dis.height - x2;
	x22 = y2

	d.swipe(x11, y11, x22, y22, 0.5);

def buchongtili(d):
	click_image(d, "tili_menu.750x1334.png")
	if click_image(d, "tilibuzu_qianwang.750x1334.png"):
		print("tilibuzu")
		click_image(d, "queding.750x1334.png")
	if click_image(d, "buchongtili.750x1334.png"):
		print("swipe")
		swipe(d, 224, 640, 468, 672)
		time.sleep(2);
		click(d, 390, 968);
		click(d, 390, 968);
		click(d, 390, 968);
		click(d, 236, 960)
		click(d, 236, 960)
		click(d, 236, 960)
		click_image(d, "close.750x1334.png")
	if click_image(d, "tilibuzu.750x1334.png"):
		click_image(d, "queding.750x1334.png")

def enter_huodong(d):
	if (click_image(d, "menu.750x1334.png") != None) | (click_image(d, "menu2.750x1334.png") != None):
		print("click menu")
		time.sleep(1);
	if click_image(d, "huodong_start.750x1334.png"):
		print("huodong start")

def enter_liulihuanjing(d):
	enter_huodong(d);
	if click_image(d, "liulihuanjing.750x1334.png"):
		print("enter liu li huan jing")
		time.sleep(2);

def enter_liulihuanjing_putong(d):
	enter_liulihuanjing(d);
	if click_image(d, "liuli_putong.750x1334.png"):
		print("click liuli_putong");
		time.sleep(1);

def enter_liulihuanjing_kunnan(d):
	enter_liulihuanjing(d);
	if click_image(d, "liuli_kunnan.750x1334.png"):
		print("click liuli kunnan");
		time.sleep(1);

def enter_liulihuanjing_putong_hebo(d):
	enter_liulihuanjing_putong(d);
	if click_image(d, "hebo.750x1334.png"):
		print("click hebo")
		time.sleep(1);
		click_image(d, "danren.750x1334.png");
		while 1:
			buchongtili(d)
			# if click_image(d, "level5.750x1334.png"):
			# 	print("chose level5")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "10_10.750x1334.png"):
			# 	print("chose 10 10")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "level4.750x1334.png"):
			# 	print("chose level4")
			# 	break;
			# elif click_image(d, "level3.750x1334.png"):
			# 	print("chose level3")
			# 	break;
			# else :
			# 	pass;
			print("rechose")
			click(d, 336, 314)#点第一个
			time.sleep(1)
			break;

		while 1:
			print("start kaiqifuben")
			if click_image(d, "kaiqifuben.750x1334.png"):
				print("did start kaiqifuben")
				break;
		gongji(d)
	click_image(d, "jixu.750x1334.png")
	click_image(d, "jixu.750x1334.png")
	click_image(d, "queding.750x1334.png")

def sucai_huo(d):
	enter_huodong(d);
	click_image(d, "wuxingxiulian.750x1334.png")
	click_image(d, "sucai_huo_gaoji.750x1334.png")
	buchongtili(d)
	if click_image(d, "kaishixiulian.750x1334.png"):
		time.sleep(2)
		print("start chose zhuzhan")
		while 1:
			buchongtili(d)
			# if click_image(d, "level5.750x1334.png"):
			# 	print("chose level5")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "10_10.750x1334.png"):
			# 	print("chose 10 10")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "level4.750x1334.png"):
			# 	print("chose level4")
			# 	break;
			# elif click_image(d, "level3.750x1334.png"):
			# 	print("chose level3")
			# 	break;
			# else :
			# 	pass;
			print("rechose")
			click(d, 336, 314)#点第一个
			time.sleep(1)
			break;

		while 1:
			print("start kaiqifuben")
			buchongtili(d)
			if click_image(d, "kaiqifuben.750x1334.png"):
				print("did start kaiqifuben")
				break;

		gongji(d)
		
	click_image(d, "jixu.750x1334.png")
	click_image(d, "jixu.750x1334.png")
	click_image(d, "queding.750x1334.png")
	

def zudui(d):
	while click_image(d, "pipei.750x1334.png"):
		click(d, 336, 314)#点第一个
		click_image(d, "zhunbei.750x1334.png")

	click_image(d, "close.750x1334.png")
	if click_image(d, "kaishishouyao.750x1334.png") != None:
			print("kaishishouyao")
	
	click(d, 598, 46)
	click(d, 398, 1046)
	click(d, 398, 1160)
	click(d, 398, 1260)
	click(d, 58, 1056)
	click_image(d, "queding_buchong.750x1334.png")
	buchongtili(d)
	click(d, 598, 46)
	click(d, 398, 1046)
	click(d, 398, 1160)
	click(d, 398, 1260)
	click(d, 58, 1056)
	click_image(d, "jixu.750x1334.png")
	click(d, 598, 46)
	click(d, 398, 1046)
	click(d, 398, 1160)
	click(d, 398, 1260)
	click(d, 58, 1056)
	click_image(d, "jixu.750x1334.png")
	click(d, 598, 46)
	click(d, 398, 1046)
	click(d, 398, 1160)
	click(d, 398, 1260)
	click(d, 58, 1056)
	click_image(d, "queding.750x1334.png")

def enter_liulihuanjing_kunnan_tushanye(d):
	enter_liulihuanjing_kunnan(d);
	if click_image(d, "kunnan_tushanye.750x1334.png"):
		print("click tushanye")
		time.sleep(1);
		click_image(d, "danren.750x1334.png");
		while 1:
			buchongtili(d)
			# if click_image(d, "level5.750x1334.png"):
			# 	print("chose level5")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "10_10.750x1334.png"):
			# 	print("chose 10 10")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "level4.750x1334.png"):
			# 	print("chose level4")
			# 	break;
			# elif click_image(d, "level3.750x1334.png"):
			# 	print("chose level3")
			# 	break;
			# else :
			# 	pass;
			print("rechose")
			click(d, 336, 314)#点第一个
			time.sleep(1)
			break;

		while 1:
			print("start kaiqifuben")
			if click_image(d, "kaiqifuben.750x1334.png"):
				print("did start kaiqifuben")
				break;
		gongji(d)
	click_image(d, "jixu.750x1334.png")
	click_image(d, "jixu.750x1334.png")
	click_image(d, "queding.750x1334.png")

def muqing2(d):
	enter_huodong(d)
	click_image(d, "zhiquxingcheng.750x1334.png")
	click_image(d, "chongfengzhishi_rukou.750x1334.png")
	click_image(d, "chongfengzhishi_4.750x1334.png")
	buchongtili(d)
	if click_image(d, "tiaozhan.1334x750.png"):
		time.sleep(2)
		print("start chose zhuzhan")
		while 1:
			buchongtili(d)
			if click_image(d, "level5.750x1334.png"):
				print("chose level5")
				time.sleep(1);
				break;
			elif click_image(d, "10_10.750x1334.png"):
				print("chose 10 10")
				time.sleep(1);
				break;
			elif click_image(d, "batianlong_tu.750x1334.png"):
				print("chose batianlong tu")
				time.sleep(1);
				break;
			# elif click_image(d, "level4.750x1334.png"):
			# 	print("chose level4")
			# 	break;
			# elif click_image(d, "level3.750x1334.png"):
			# 	print("chose level3")
			# 	break;
			else :
				pass;

			print("rechose")
			click(d, 336, 314)#点第一个
			time.sleep(1)
			click(d, 404, 602)#重新选助战

		while 1:
			print("start kaiqifuben")
			if click_image(d, "kaiqifuben.750x1334.png"):
				print("did start kaiqifuben")
				break;

		gongji(d)
		
	click_image(d, "kaishishouyao.750x1334.png")
	click_image(d, "jixu.750x1334.png")
	click_image(d, "jixu.750x1334.png")
	click_image(d, "queding.750x1334.png")
	
def shuye_jinmu(d):
	enter_huodong(d);
	click_image(d, "wuxingxiulian.750x1334.png")
	click_image(d, "shuye_tumu_teji.750x1334.png")
	buchongtili(d)
	if click_image(d, "kaishixiulian.750x1334.png"):
		time.sleep(2)
		print("start chose zhuzhan")
		while 1:
			buchongtili(d)
			# if click_image(d, "level5.750x1334.png"):
			# 	print("chose level5")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "10_10.750x1334.png"):
			# 	print("chose 10 10")
			# 	time.sleep(1);
			# 	break;
			# elif click_image(d, "level4.750x1334.png"):
			# 	print("chose level4")
			# 	break;
			# elif click_image(d, "level3.750x1334.png"):
			# 	print("chose level3")
			# 	break;
			# else :
			# 	pass;
			print("rechose")
			click(d, 336, 314)#点第一个
			time.sleep(1)
			break;

		while 1:
			print("start kaiqifuben")
			buchongtili(d)
			if click_image(d, "kaiqifuben.750x1334.png"):
				print("did start kaiqifuben")
				break;

		gongji(d)
		
	click_image(d, "jixu.750x1334.png")
	click_image(d, "jixu.750x1334.png")
	click_image(d, "queding.750x1334.png")
	

d = atx.connect('http://192.168.0.102:8100', platform='ios') # platform也可以不指定
print d.rotation
dis = d.display
while 1:
	muqing2(d)


#d.click_image("tiaozhan.1334x750.png")