
import java.awt.image.*;
import java.io.File;
import java.io.IOException;

import java.awt.Color;
import javax.imageio.ImageIO;

public class ImageSalt {

    public ImageSalt() {
        super();
        BufferedImage image = null;

        try {

            // Read from a file
            File file = new File("gaussian1.png");

            image = ImageIO.read(file);
        } catch (IOException e) {

            System.err.println("Cannot open the file.");
        }

        System.out.println("Width: " + image.getWidth());
        System.out.println("Height: " + image.getHeight());

        BufferedImage image2 = new BufferedImage(image.getWidth(), image.getHeight(), BufferedImage.TYPE_INT_RGB);

        int rgb[][] = new int[image.getWidth()][image.getHeight()];
        Color[] pixel = new Color[9];
        int[] R = new int[9];
        int[] B = new int[9];
        int[] G = new int[9];
        int total = 0;
        for (int i = 1; i < image.getWidth() - 1; i++)
            for (int j = 1; j < image.getHeight() - 1; j++) {
                pixel[0] = new Color(image.getRGB(i - 1, j - 1));
                pixel[1] = new Color(image.getRGB(i - 1, j));
                pixel[2] = new Color(image.getRGB(i - 1, j + 1));
                pixel[3] = new Color(image.getRGB(i, j + 1));
                pixel[4] = new Color(image.getRGB(i + 1, j + 1));
                pixel[5] = new Color(image.getRGB(i + 1, j));
                pixel[6] = new Color(image.getRGB(i + 1, j - 1));
                pixel[7] = new Color(image.getRGB(i, j - 1));
                pixel[8] = new Color(image.getRGB(i, j));
                for (int k = 0; k < 9; k++) {
                    R[k] = pixel[k].getRed();
                    B[k] = pixel[k].getBlue();
                    G[k] = pixel[k].getGreen();
                    total += R[k] + B[k] + G[k];
                }

                rgb[i][j] = averageRGB(image.getRGB(i, j));
                System.out.print(rgb[i][j] + " ");
            }

        for (int i = 0; i < image.getWidth(); i++)
            for (int j = 0; j < image.getHeight(); j++) {
                image2.setRGB(i, j, averageRGB2(rgb[i][j]));
            }

        try {
            writeImage(image2);
        } catch (ImagingOpException e) {

            e.printStackTrace();
        }

    }

    public int averageRGB(int rgb) {
        int r = (rgb >> 16) & 0xff;
        int g = (rgb >> 8) & 0xff;
        int b = (rgb >> 0) & 0xff;

        int nIntensity = (int) ((r + g + b) / 3);
        r = g = b = nIntensity;
        return nIntensity;
    }

    public int averageRGB2(int rgb) {

        int r = (rgb & 0xff) << 16;
        int g = (rgb & 0xff) << 8;
        int b = (rgb & 0xff);

        int nIntensity = (int) (r + g + b);
        r = g = b = nIntensity;
        return (rgb & 0xff000000) | (r << 16) | (g << 8) | (b << 0);

    }

    public void writeImage(BufferedImage img) {
        File f = new File("my_Salt3.png");
        try {
            ImageIO.write(img, "png", f);
        } catch (IOException e) {

            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        new ImageSalt();
    }
}