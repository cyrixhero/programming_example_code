// �򥻤���
public interface ISimpleBase
{
    string GetBase();
}
// �~�Ӧ� ISimpleBase ������
public interface ISimpleTest : ISimpleBase
{
    string GetName();
}
