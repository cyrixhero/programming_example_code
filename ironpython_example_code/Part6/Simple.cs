using System;
using System.Collections;
// �x�s�u��ƪ����O
public class Simple : IEnumerable {
    private int data;
    public Simple(int data) {
        this.data = data;
    }
    // �ഫ���r�ꪺ��k
    public override string ToString() {
        return String.Format("Simple<{0}>", data);
    }
    // �w�q iterator
    public IEnumerator GetEnumerator() {
        for (int i = 0; i < data; i ++) {
            yield return new Simple(i);
        }
    }
    // �w�q�B��l (�[�k�B��l)
    public static Simple operator +(Simple a, Simple b) {
        return new Simple(a.data + b.data);
    }
}
