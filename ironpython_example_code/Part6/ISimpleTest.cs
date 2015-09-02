// 基本介面
public interface ISimpleBase
{
    string GetBase();
}
// 繼承自 ISimpleBase 的介面
public interface ISimpleTest : ISimpleBase
{
    string GetName();
}
