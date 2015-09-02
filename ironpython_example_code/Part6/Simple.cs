using System;
using System.Collections;
// 儲存短整數的類別
public class Simple : IEnumerable {
    private int data;
    public Simple(int data) {
        this.data = data;
    }
    // 轉換成字串的方法
    public override string ToString() {
        return String.Format("Simple<{0}>", data);
    }
    // 定義 iterator
    public IEnumerator GetEnumerator() {
        for (int i = 0; i < data; i ++) {
            yield return new Simple(i);
        }
    }
    // 定義運算子 (加法運算子)
    public static Simple operator +(Simple a, Simple b) {
        return new Simple(a.data + b.data);
    }
}
