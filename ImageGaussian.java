
import java.awt.image.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ImageGaussian {

    public ImageGaussian() {
        super();

        BufferedImage image = null;

        try {

            File file = new File("Gaussian1.png");
            image = ImageIO.read(file);
        } catch (IOException e) {

            System.err.println("Cannot open the file.");
        }

        System.out.println("Width: " + image.getWidth());
        System.out.println("Height: " + image.getHeight());

        BufferedImage image2 = new BufferedImage(image.getWidth(), image.getHeight(), BufferedImage.TYPE_INT_RGB);

        int rgb[][] = new int[image.getWidth()][image.getHeight()];
        int sum = 0;

        for (int i = 1; i < image.getWidth() - 1; i++) {
            for (int j = 1; j < image.getHeight() - 1; j++) {
                sum = (rgb[i - 1][j - 1] +
                        rgb[i][j - 1] +
                        rgb[i + 1][j - 1] +
                        rgb[i - 1][j] +
                        rgb[i][j] +
                        rgb[i + 1][j] +
                        rgb[i - 1][j + 1] +
                        rgb[i][j + 1] +
                        rgb[i + 1][j + 1]) / 9;
                rgb[i][j] = sum;
            }
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

        int nIntensity = (int) ((r * 0.299) + (g * 0.587) + (b * 0.114));
        // int nIntensity = (int) ((r) + (g) + (b)) / 3;
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
        File f = new File("my_Gaussian1.png");
        try {
            ImageIO.write(img, "png", f);
        } catch (IOException e) {

            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        new ImageGaussian();
    }
}
