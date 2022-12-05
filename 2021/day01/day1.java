package day01;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class day1 {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Write filename as parameter.");
            System.exit(0);
        }
        // Change strings into integers
        var data = ReadData(args[0]).stream().map(Integer::parseInt).collect(Collectors.toList());

        System.out.println(Part1(data));
        System.out.println(Part2(data));
    }

    static int Part1(List<Integer> data) {
        int counter = 0;
        int previous = data.get(0);
        for (int value : data.subList(1, data.size())) {
            if (value > previous)
                counter++;
            previous = value;
        }
        return counter;
    }

    static int Part2(List<Integer> data) {
        int counter = 0;
        int previous = Integer.MAX_VALUE;
        for (int i = 0; i < data.size() - 2; i++) {
            var value = IntStream.range(i, i + 3).mapToObj(data::get).collect(Collectors.summingInt(m -> m));
            if (value > previous)
                counter++;
            previous = value;
        }
        return counter;
    }

    /// Read file and save into list of strings
    static List<String> ReadData(String filename) {
        try {
            var lines = Files.readAllLines(Path.of(filename));
            Optional.ofNullable(lines).orElseThrow();
            return lines;

        } catch (IOException e) {
            System.out.println("Wrong file name.");
            System.exit(0);
        }
        return null;
    }
}