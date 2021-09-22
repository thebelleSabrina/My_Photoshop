"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:(SimpleImage) the original image
    :return: a new blurred image based on original image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            blank_p = new_img.get_pixel(x, y)  # create a blank canvas
            if x == 0 and y == 0:  # left upper corner
                img_p0 = img.get_pixel(x, y)
                img_p1 = img.get_pixel(x+1, y)
                img_p2 = img.get_pixel(x, y+1)
                img_p3 = img.get_pixel(x+1, y+1)
                blank_p.red = (img_p0.red+img_p1.red+img_p2.red+img_p3.red)//4
                blank_p.green = (img_p0.green + img_p1.green + img_p2.green + img_p3.green) // 4
                blank_p.blue = (img_p0.blue + img_p1.blue + img_p2.blue + img_p3.blue) // 4
            elif x == int(img.width-1) and y == 0:  # right upper corner
                img_p4 = img.get_pixel(x, y)
                img_p5 = img.get_pixel(x-1, y)
                img_p6 = img.get_pixel(x, y+1)
                img_p7 = img.get_pixel(x-1, y+1)
                blank_p.red = (img_p4.red + img_p5.red + img_p6.red + img_p7.red) // 4
                blank_p.green = (img_p4.green + img_p5.green + img_p6.green + img_p7.green) // 4
                blank_p.blue = (img_p4.blue + img_p5.blue + img_p6.blue + img_p7.blue) // 4
            elif x == 0 and y == int(img.height-1):  # left lower corner
                img_p8 = img.get_pixel(x, y)
                img_p9 = img.get_pixel(x+1, y)
                img_p10 = img.get_pixel(x+1, y-1)
                img_p11 = img.get_pixel(x, y-1)
                blank_p.red = (img_p8.red + img_p9.red + img_p10.red + img_p11.red) // 4
                blank_p.green = (img_p8.green + img_p9.green + img_p10.green + img_p11.green) // 4
                blank_p.blue = (img_p8.blue + img_p9.blue + img_p10.blue + img_p11.blue) // 4
            elif x == int(img.width-1) and y == int(img.height-1):  # right lower corner
                img_p12 = img.get_pixel(x, y)
                img_p13 = img.get_pixel(x, y-1)
                img_p14 = img.get_pixel(x-1, y)
                img_p15 = img.get_pixel(x-1, y-1)
                blank_p.red = (img_p12.red + img_p13.red + img_p14.red + img_p15.red) // 4
                blank_p.green = (img_p12.green + img_p13.green + img_p14.green + img_p15.green) // 4
                blank_p.blue = (img_p12.blue + img_p13.blue + img_p14.blue + img_p15.blue) // 4
            elif y == 0:  # get upper side's pixel
                img_pa = img.get_pixel(x, y)
                img_pb = img.get_pixel(x-1, y)
                img_pc = img.get_pixel(x-1, y+1)
                img_pd = img.get_pixel(x, y + 1)
                img_pe = img.get_pixel(x+1, y)
                img_pf = img.get_pixel(x+1, y+1)
                blank_p.red = (img_pa.red + img_pb.red + img_pc.red + img_pd.red + img_pe.red + img_pf.red) // 6
                blank_p.green = (img_pa.green + img_pb.green + img_pc.green + img_pd.green + img_pe.green + img_pf.green) // 6
                blank_p.blue = (img_pa.blue + img_pb.blue + img_pc.blue + img_pd.blue + img_pe.blue + img_pf.blue) // 6
            elif y == int(img.height-1):  # get lower side's pixel
                img_pg = img.get_pixel(x, y)
                img_ph = img.get_pixel(x-1, y)
                img_pi = img.get_pixel(x+1, y)
                img_pj = img.get_pixel(x, y-1)
                img_pk = img.get_pixel(x-1, y-1)
                img_pl = img.get_pixel(x+1, y-1)
                blank_p.red = (img_pg.red + img_ph.red + img_pi.red + img_pj.red + img_pk.red + img_pl.red) // 6
                blank_p.green = (img_pg.green + img_ph.green + img_pi.green + img_pj.green + img_pk.green + img_pl.green) // 6
                blank_p.blue = (img_pg.blue + img_ph.blue + img_pi.blue + img_pj.blue + img_pk.blue + img_pl.blue) // 6
            elif x == 0:  # get left side's pixel
                img_pm = img.get_pixel(x, y)
                img_pn = img.get_pixel(x, y-1)
                img_po = img.get_pixel(x+1, y-1)
                img_pp = img.get_pixel(x+1, y)
                img_pq = img.get_pixel(x+2, y-1)
                img_pr = img.get_pixel(x+2, y)
                blank_p.red = (img_pm.red + img_pn.red + img_po.red + img_pp.red + img_pq.red + img_pr.red) // 6
                blank_p.green = (img_pm.green + img_pn.green + img_po.green + img_pp.green + img_pq.green + img_pr.green) // 6
                blank_p.blue = (img_pm.blue + img_pn.blue + img_po.blue + img_pp.blue + img_pq.blue + img_pr.blue) // 6
            elif x == int(img.width-1):  # get right side's pixel
                img_ps = img.get_pixel(x, y)
                img_pt = img.get_pixel(x, y-1)
                img_pu = img.get_pixel(x-1, y-1)
                img_pv = img.get_pixel(x-1, y)
                img_pw = img.get_pixel(x, y+1)
                img_px = img.get_pixel(x-1, y+1)
                blank_p.red = (img_ps.red + img_pt.red + img_pu.red + img_pv.red + img_pw.red + img_px.red) // 6
                blank_p.green = (img_ps.green + img_pt.green + img_pu.green + img_pv.green + img_pw.green + img_px.green) // 6
                blank_p.blue = (img_ps.blue + img_pt.blue + img_pu.blue + img_pv.blue + img_pw.blue + img_px.blue) // 6
            else:   # the rest of pixel
                img_n0 = img.get_pixel(x, y)
                img_n1 = img.get_pixel(x-1, y)
                img_n2 = img.get_pixel(x+1, y)
                img_n3 = img.get_pixel(x-1, y-1)
                img_n4 = img.get_pixel(x, y-1)
                img_n5 = img.get_pixel(x+1, y-1)
                img_n6 = img.get_pixel(x-1, y+1)
                img_n7 = img.get_pixel(x, y+1)
                img_n8 = img.get_pixel(x+1, y+1)
                blank_p.red = (img_n0.red + img_n1.red + img_n2.red + img_n3.red + img_n4.red + img_n5.red + img_n6.red + img_n7.red + img_n8.red) // 9
                blank_p.green = (img_n0.green + img_n1.green + img_n2.green + img_n3.green+img_n4.green+img_n5.green + img_n6.green + img_n7.green+ img_n8.green) // 9
                blank_p.blue = (img_n0.blue + img_n1.blue + img_n2.blue + img_n3.blue + img_n4.blue + img_n5.blue + img_n6.blue + img_n7.blue + img_n8.blue) // 9
    return new_img


def main():
    """
    This programs creates the original image's blurred version.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
