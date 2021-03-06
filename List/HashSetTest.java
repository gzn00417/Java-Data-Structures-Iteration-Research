package List;

import org.junit.*;
import java.util.*;

public class HashSetTest {

	private static HashSet<String> list = new HashSet<>();
	private final static int N = 1000000, M = 100;
	private final static String STR = "abcdefg";

	@BeforeClass
	public static void CreateList() {
		for (int i = 0; i < N; i++) {
			list.add(STR + String.valueOf((int) (Math.random() * N)));
		}
	}

	//@Test
	public void FOR() {
		for (int k = 0; k < M; k++) {
			for (int i = 0; i < list.size(); i++) {
				String str = list.get(i);
			}
		}
	}

	@Test
	public void Inner_Iteration() {
		for (int k = 0; k < M; k++) {
			for (String str : list) {
				String s = str;
			}
		}
	}

	@Test
	public void Explicit_Iteration() {
		for (int k = 0; k < M; k++) {
			Iterator<String> it = list.iterator();
			while (it.hasNext()) {
				String str = it.next();
			}
		}
	}
}
