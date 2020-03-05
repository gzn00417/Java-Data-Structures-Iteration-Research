package List;

import org.junit.*;
import java.util.*;

public class HashMapTest {

	private static HashMap<Integer, String> list = new HashMap<>();
	private final static int N = 1000000, M = 10;
	private final static String STR = "abcdefg";

	@BeforeClass
	public static void CreateList() {
		for (int i = 0; i < N; i++) {
			list.put((int)(Math.random()*N), STR+String.valueOf((int)(Math.random()*N)));
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
			for (Integer i : list.keySet()) {
				String s = list.get(i);
			}
		}
	}

	@Test
	public void Explicit_Iteration() {
		for (int k = 0; k < M; k++) {
			Iterator<Integer> it = list.keySet().iterator();
			while (it.hasNext()) {
				String str = list.get(it.next());
			}
		}
	}
}
