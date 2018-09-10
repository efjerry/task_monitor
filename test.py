# -*- coding:utf-8 -*-
import os, shutil


def get_files(root, target, num):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            files.append(dirpath + '/' + filename)

    files.sort(key=lambda fn: os.path.getmtime(fn), reverse=True)

    for i in files[:num]:
        if not os.path.exists(target):
            os.makedirs(target)
        shutil.copy(i, target + os.path.split(i)[1])


if __name__ == '__main__':
    all_file = [['/locallog/xxx/232A60C5-E78D-49E4-A941-37209C331A65', '/locallog/tmp/1-查询项目信息-00-SD00102-232A60C5-E78D-49E4-A941-37209C331A65'],
                ['/locallog/xxx/7017FEFC-3EFA-431D-9F50-69AB570D84F6', '/locallog/tmp/3-查询年度投资计划信息-00-SD00100-7017FEFC-3EFA-431D-9F50-69AB570D84F6'],
                ['/locallog/xxx/794AE12E-2609-4DA8-AD34-F9AB1A53F30F', '/locallog/tmp/6-接收项目前期费资金支付-00-SD00104-794AE12E-2609-4DA8-AD34-F9AB1A53F30F'],
                ['/locallog/xxx/F40439EA-BEBF-4C61-8B2B-7948CB38BD29', '/locallog/tmp/7-同步工程项目概预算信息-00-SD00153-F40439EA-BEBF-4C61-8B2B-7948CB38BD29'],
                ['/locallog/xxx/F4EF625D-92CC-49E4-BE66-4F3132BB03BB', '/locallog/tmp/8-同步工程合同信息和工程项目资金任务分解（有合同部分）信息-00-SD00152-F4EF625D-92CC-49E4-BE66-4F3132BB03BB'],
                ['/locallog/xxx/595D6CB2-DE35-43DD-B4F2-A2A22B0841E8', '/locallog/tmp/9-同步工程项目发票和资金任务分解（无合同部分）信息-00-SD00171-595D6CB2-DE35-43DD-B4F2-A2A22B0841E8'],
                ['/locallog/xxx/58A4F0A0-741A-4B90-A5FC-D0A3265EA5D4', '/locallog/tmp/10-同步工程项目进度结算信息-00-SD00154-58A4F0A0-741A-4B90-A5FC-D0A3265EA5D4'],
                ['/locallog/xxx/95E7CF2A-3970-471D-8BDA-FFCB02BCE36A', '/locallog/tmp/11-查询财务管理系统发票对应的付款申请情况-00-SD00151-95E7CF2A-3970-471D-8BDA-FFCB02BCE36A'],
                ['/locallog/xxx/06811510-96B9-4A9F-9A6D-89B40995E7C8', '/locallog/tmp/12-接收付款结果信息-00-SD00098-06811510-96B9-4A9F-9A6D-89B40995E7C8'],
                ['/locallog/xxx/8BE15F75-F405-419C-8750-D790C6FB2D6D', '/locallog/tmp/13-同步付款结果信息-00-SD00119-8BE15F75-F405-419C-8750-D790C6FB2D6D'],
                ['/locallog/xxx/FCD9C808-5703-499D-BF50-88191330D4E6', '/locallog/tmp/14-同步物资·工程项目资金任务分解（无合同部分）信息-00-SD00158-FCD9C808-5703-499D-BF50-88191330D4E6'],
                ['/locallog/xxx/D7C200EA-7F45-4DF4-874E-B97649FB866F', '/locallog/tmp/15-同步物资·工程项目资金任务分解（有合同部分）信息-00-SD00167-D7C200EA-7F45-4DF4-874E-B97649FB866F'],
                ['/locallog/xxx/DB721B9A-C2E3-498D-B59C-5F51F36F82D0', '/locallog/tmp/16-同步物资发票信息-00-SD00166-DB721B9A-C2E3-498D-B59C-5F51F36F82D0'],
                ['/locallog/xxx/9E2E7326-1E90-44CC-A41B-E2C636D73CE0', '/locallog/tmp/17-同步付款申请结果-00-SD00105-9E2E7326-1E90-44CC-A41B-E2C636D73CE0'],
                ['/locallog/xxx/E26817B9-C92C-43BC-9B08-D5230A88BF77', '/locallog/tmp/18-同步逆向操作付款结果-00-SD00106-E26817B9-C92C-43BC-9B08-D5230A88BF77'],
                ['/locallog/xxx/E0DD7175-0515-403B-836A-456B0EDC8680', '/locallog/tmp/19-同步工程项目竣工验收设备资产清单信息-00-SD00155-E0DD7175-0515-403B-836A-456B0EDC8680'],
                ['/locallog/xxx/BDDB0969-1258-40BE-AAFC-8EB19140CA5C', '/locallog/tmp/20-查询修理项目关联设备清单-00-SD00103-BDDB0969-1258-40BE-AAFC-8EB19140CA5C'],
                ['/locallog/xxx/A21AA0DD-C7FC-4A53-9B16-5BCDFAD1ED0C', '/locallog/tmp/21-同步工程项目结算报告（工程结算数据）信息-00-SD00156-A21AA0DD-C7FC-4A53-9B16-5BCDFAD1ED0C'],
                ['/locallog/xxx/9C1E5929-F1E8-4FE4-9678-EE3DF6D44DB9', '/locallog/tmp/22-回写资产卡片价值数据-00-SD00037-9C1E5929-F1E8-4FE4-9678-EE3DF6D44DB9'],
                ['/locallog/xxx/E0BDE221-63A4-49D0-9785-B7B38B216855', '/locallog/tmp/24-同步工程项目验收报告信息-00-SD00157-E0BDE221-63A4-49D0-9785-B7B38B216855'],
                ['/locallog/xxx/E38276EE-948C-441F-B504-4C8D1B5687BB', '/locallog/tmp/25-接收建设贷款利息集成-00-SD00099-E38276EE-948C-441F-B504-4C8D1B5687BB'],
                ['/locallog/xxx/06E085EB-2196-4224-9CE2-27E16A95A340', '/locallog/tmp/26-同步物资入库数据信息-00-SD00169-06E085EB-2196-4224-9CE2-27E16A95A340'],
                ['/locallog/xxx/BB0B6F7F-E382-41ED-AA96-5B502D6923EE', '/locallog/tmp/27-同步物资出库数据信息-00-SD00165-BB0B6F7F-E382-41ED-AA96-5B502D6923EE'],
                ['/locallog/xxx/30E4FAAB-5D90-4E25-81CC-93D6F06B0A98', '/locallog/tmp/28-同步物资盘点数据信息-00-SD00168-30E4FAAB-5D90-4E25-81CC-93D6F06B0A98'],
                ['/locallog/xxx/49AEABBE-7AC2-478F-AD43-70B53D791B30', '/locallog/tmp/29-同步物资调拨数据信息-00-SD00170-49AEABBE-7AC2-478F-AD43-70B53D791B30'],
                ['/locallog/xxx/DF2A2A76-AB89-4507-8CE4-ADCBD506EB7F', '/locallog/tmp/30-同步设备台帐变更申请信息-00-SD00038-DF2A2A76-AB89-4507-8CE4-ADCBD506EB7F'],
                ['/locallog/xxx/48B8C639-4DE8-4736-9B4F-5ED5E4C9B292', '/locallog/tmp/31-同步设备台账信息变更单-00-SD00162-48B8C639-4DE8-4736-9B4F-5ED5E4C9B292'],
                ['/locallog/xxx/7CD8618C-A7D8-4397-BACA-548144F158CF', '/locallog/tmp/32-同步资产其他减少接口-00-SD00160-7CD8618C-A7D8-4397-BACA-548144F158CF'],
                ['/locallog/xxx/2D1ACC1A-95A3-4470-8EA8-5C239CD61FEC', '/locallog/tmp/33-同步资产其他增加接口-00-SD00161-2D1ACC1A-95A3-4470-8EA8-5C239CD61FEC'],
                ['/locallog/xxx/26077B38-6119-44F0-8F4A-FA6046F3F22B', '/locallog/tmp/34-同步财务系统分摊资产技改成本信息-00-SD00036-26077B38-6119-44F0-8F4A-FA6046F3F22B'],
                ['/locallog/xxx/5BB771A6-001A-4543-8A8F-389866D65160', '/locallog/tmp/35-同步资产级设备的项目费用成本信息-00-SD00039-5BB771A6-001A-4543-8A8F-389866D65160'],
                ['/locallog/xxx/982FC527-9A43-4E0B-BDDF-69EEF9895A55', '/locallog/tmp/36-同步财务系统归集修理（抢修）项目资产分摊成本信息服务-00-SD00040-982FC527-9A43-4E0B-BDDF-69EEF9895A55'],
                ['/locallog/xxx/5F6CC94B-78D8-49D3-AEE2-3EDF07839D07', '/locallog/tmp/37-同步资产级设备运维成本-00-SD00042-5F6CC94B-78D8-49D3-AEE2-3EDF07839D07'],
                ['/locallog/xxx/EFADB01B-DCA5-4254-9856-6C405EC423C7', '/locallog/tmp/38-查询设备退役计划-00-SD00101-EFADB01B-DCA5-4254-9856-6C405EC423C7'],
                ['/locallog/xxx/83DD7BD6-36ED-4312-9AFE-ADD5A8503357', '/locallog/tmp/39-同步报废预算信息-00-SD00041-83DD7BD6-36ED-4312-9AFE-ADD5A8503357'],
                ['/locallog/xxx/609C73B0-1E82-4166-AE54-4181742C7F5A', '/locallog/tmp/40-同步报废设备清单-00-SD00148-609C73B0-1E82-4166-AE54-4181742C7F5A'],
                ['/locallog/xxx/AA49BE9D-B4C7-4A97-81F1-2CB571284BF2', '/locallog/tmp/42-同步报废物资入库数据信息-00-SD00150-AA49BE9D-B4C7-4A97-81F1-2CB571284BF2'],
                ['/locallog/xxx/CC5523E1-3F55-4D7A-B5A7-1A7146934AFF', '/locallog/tmp/43-同步报废物资出库数据信息-00-SD00149-CC5523E1-3F55-4D7A-B5A7-1A7146934AFF'],
                ['/locallog/xxx/0CC16B8C-8751-436E-ABA4-A03C9747E739', '/locallog/tmp/44-同步公网通信资源租用预算编制（调整）数信息-00-SD00159-0CC16B8C-8751-436E-ABA4-A03C9747E739'],
                ['/locallog/xxx/3D49BF5C-B21F-4626-B43D-B6B24D76FF1C', '/locallog/tmp/45-统计新增固定资产情况-00-SD00163-3D49BF5C-B21F-4626-B43D-B6B24D76FF1C'],
                ['/locallog/xxx/ABFE1909-A72A-4DD8-8873-746C8CA4BCB5', '/locallog/tmp/46-统计资金支付、资金到位情况-00-SD00164-ABFE1909-A72A-4DD8-8873-746C8CA4BCB5'],
                ['/locallog/xxx/605EE22C-00A8-4B97-930C-2B66F8EC1FF6', '/locallog/tmp/48-同步工资薪酬支付数据-00-SD00129-605EE22C-00A8-4B97-930C-2B66F8EC1FF6'],
                ['/locallog/xxx/6B028555-A3FA-440A-AD2C-269C3A0E6ADA', '/locallog/tmp/49-同步支付结果反馈（人资）数据-00-SD00202-6B028555-A3FA-440A-AD2C-269C3A0E6ADA'],
                ['/locallog/xxx/64184382-9466-43C1-BDD6-7D43EA5A4ABB', '/locallog/tmp/50-同步社会保险费支付数据-00-SD00122-64184382-9466-43C1-BDD6-7D43EA5A4ABB'],
                ['/locallog/xxx/C5677F19-B396-430D-A2E3-8F0055E36462', '/locallog/tmp/51-同步住房公积金支付数据-00-SD00120-C5677F19-B396-430D-A2E3-8F0055E36462'],
                ['/locallog/xxx/BF2039E7-AAE5-44DB-A7D3-2A0768E36BF6', '/locallog/tmp/52-同步企业年金支付数据-00-SD00124-BF2039E7-AAE5-44DB-A7D3-2A0768E36BF6'],
                ['/locallog/xxx/26B16419-6BB6-4DFD-B5DB-6650922E8595', '/locallog/tmp/53-发布月度会计报表相关指标信息-00-SD00201-26B16419-6BB6-4DFD-B5DB-6650922E8595'],
                ['/locallog/xxx/DB4F2DBA-E717-43A4-8B0C-A30FB8881AAC', '/locallog/tmp/54-发布经济效益指标预算报表发布数据信息-00-SD00199-DB4F2DBA-E717-43A4-8B0C-A30FB8881AAC'],
                ['/locallog/xxx/F2626459-8306-4369-971F-393588969F5C', '/locallog/tmp/55-同步人工成本预算编制（调整）数据-00-SD00123-F2626459-8306-4369-971F-393588969F5C'],
                ['/locallog/xxx/79CA130C-7697-4B2C-874E-8983A16EF3FD', '/locallog/tmp/56-同步工资总额人资下达数据-00-SD00128-79CA130C-7697-4B2C-874E-8983A16EF3FD'],
                ['/locallog/xxx/E9AAA204-C6F0-45B4-A275-D0994323A6BB', '/locallog/tmp/57-发布人工成本预算数据-00-SD00200-E9AAA204-C6F0-45B4-A275-D0994323A6BB'],
                ['/locallog/xxx/61A02690-6A8B-4EE6-B82D-57F25F6B285E', '/locallog/tmp/58-查询生产经营情况-00-SD00032-61A02690-6A8B-4EE6-B82D-57F25F6B285E'],
                ['/locallog/xxx/A70C6971-761E-4AB4-9CC7-73DE60577C6C', '/locallog/tmp/59-查询供电企业定员设备台帐信息-00-SD00033-A70C6971-761E-4AB4-9CC7-73DE60577C6C'],
                ['/locallog/xxx/2FF885DC-7E02-4211-98B8-109E60E75093', '/locallog/tmp/60-查询超高压主变容量信息-00-SD00034-2FF885DC-7E02-4211-98B8-109E60E75093'],
                ['/locallog/xxx/DF2ACBE0-23C7-4E80-AED8-F97CF9413DEB', '/locallog/tmp/61-同步仓库注册信息-00-SD00107-DF2ACBE0-23C7-4E80-AED8-F97CF9413DEB'],
                ['/locallog/xxx/AF5F0A99-3BDB-4B59-A422-804492D4EEFD', '/locallog/tmp/62-同步生产营销数据-00-SD00086-AF5F0A99-3BDB-4B59-A422-804492D4EEFD'],
                ['/locallog/xxx/2A5EEEF6-4A92-4B9A-918B-B3CAA68CB046', '/locallog/tmp/63-同步城区销售电量数据-00-SD00087-2A5EEEF6-4A92-4B9A-918B-B3CAA68CB046'],
                ['/locallog/xxx/E38BCCAD-15DB-456A-A3EE-D33D224A2FE0', '/locallog/tmp/64-获取计量数据-00-SD00088-E38BCCAD-15DB-456A-A3EE-D33D224A2FE0'],
                ['/locallog/xxx/BDA52FFE-AC85-4313-9660-7D5D669875AE', '/locallog/tmp/65-获取乡镇配营数据-00-SD00089-BDA52FFE-AC85-4313-9660-7D5D669875AE'],
                ['/locallog/xxx/ED6FD3CA-976D-4C16-87E9-1B289AF0E59A', '/locallog/tmp/66-提交计量验收单信息-00-SD00085-ED6FD3CA-976D-4C16-87E9-1B289AF0E59A'],
                ['/locallog/xxx/DF2250ED-79DB-4A31-BB09-E4DCEB0ED4B4', '/locallog/tmp/67-同步开箱检查结果-00-SD00117-DF2250ED-79DB-4A31-BB09-E4DCEB0ED4B4'],
                ['/locallog/xxx/C496B16C-2F49-48A4-B31D-7BF319BB328F', '/locallog/tmp/68-同步设备库位信息-00-SD00091-C496B16C-2F49-48A4-B31D-7BF319BB328F'],
                ['/locallog/xxx/13621480-7AD3-402B-BEB9-1BE2559E05CD', '/locallog/tmp/69-同步抽检计划信息-00-SD00108-13621480-7AD3-402B-BEB9-1BE2559E05CD'],
                ['/locallog/xxx/CF6BFAD0-39F1-4E6E-B611-ED045FA48784', '/locallog/tmp/70-同步强检计划信息-00-SD00110-CF6BFAD0-39F1-4E6E-B611-ED045FA48784'],
                ['/locallog/xxx/04E807FA-922A-4D5B-A7D4-08946577C474', '/locallog/tmp/71-同步抽检结果信息-00-SD00109-04E807FA-922A-4D5B-A7D4-08946577C474'],
                ['/locallog/xxx/6AF9B699-9976-488B-A647-2ED056482F39', '/locallog/tmp/72-同步强检结果信息-00-SD00111-6AF9B699-9976-488B-A647-2ED056482F39'],
                ['/locallog/xxx/6FCD0CB1-AE6E-4DCA-9A8E-AC50A97A61F2', '/locallog/tmp/73-同步闲置物资入库信息-00-SD00094-6FCD0CB1-AE6E-4DCA-9A8E-AC50A97A61F2'],
                ['/locallog/xxx/BD894CA4-2304-4853-8E74-D1F3AA22A2FC', '/locallog/tmp/74-同步设备再利用鉴定信息-00-SD00114-BD894CA4-2304-4853-8E74-D1F3AA22A2FC'],
                ['/locallog/xxx/62DAD89E-88A9-4EF1-919E-C4ABDE033B72', '/locallog/tmp/75-同步设备报废信息-00-SD00115-62DAD89E-88A9-4EF1-919E-C4ABDE033B72'],
                ['/locallog/xxx/21C924AB-2BAB-4CDE-B928-1EB370C0CF79', '/locallog/tmp/76-同步设备未装退库信息-00-SD00093-21C924AB-2BAB-4CDE-B928-1EB370C0CF79'],
                ['/locallog/xxx/1DE80AA4-E601-4B17-AA58-EF1718B89DD7', '/locallog/tmp/77-同步设备领用申请信息-00-SD00113-1DE80AA4-E601-4B17-AA58-EF1718B89DD7'],
                ['/locallog/xxx/ECE78DEA-D04E-4138-835D-C80C90D60B27', '/locallog/tmp/78-同步设备需用计划-00-SD00112-ECE78DEA-D04E-4138-835D-C80C90D60B27'],
                ['/locallog/xxx/685AA906-2B2B-4CA0-8B33-60B2F9CEB418', '/locallog/tmp/79-反馈设备领用出库信息-00-SD00092-685AA906-2B2B-4CA0-8B33-60B2F9CEB418'],
                ['/locallog/xxx/FD22D049-2864-4E7E-ACFF-6C8D307696A7', '/locallog/tmp/80-同步暂存信息-00-SD00118-FD22D049-2864-4E7E-ACFF-6C8D307696A7'],
                ['/locallog/xxx/71326B74-BF25-40B2-B0BC-E417EA009973', '/locallog/tmp/82-发送配套工程验收信息-00-SD00096-71326B74-BF25-40B2-B0BC-E417EA009973'],
                ['/locallog/xxx/0DAFEE17-AF63-4E04-B93A-0FB3C48F985B', '/locallog/tmp/83-同步计量竣工验收结论-00-SD00097-0DAFEE17-AF63-4E04-B93A-0FB3C48F985B'],
                ['/locallog/xxx/BA8D29FD-6AE6-49E5-9AE2-0A12E3F043D2', '/locallog/tmp/86-发布客服报障工单-00-SD00064-01-BA8D29FD-6AE6-49E5-9AE2-0A12E3F043D2'],
                ['/locallog/xxx/7F9625F1-1271-4615-A4AB-5FA8645DDCBF', '/locallog/tmp/87-更改客服报障工单状态-00-SD00066-7F9625F1-1271-4615-A4AB-5FA8645DDCBF'],
                ['/locallog/xxx/921187B5-2E6C-4440-BDBB-F322F0680642', '/locallog/tmp/88-发布低压故障工单-00-SD00052-01-921187B5-2E6C-4440-BDBB-F322F0680642'],
                ['/locallog/xxx/A2BA0608-ACFB-457A-8A7D-21E9F981688B', '/locallog/tmp/89-发布中压故障工单-00-SD00051-01-A2BA0608-ACFB-457A-8A7D-21E9F981688B'],
                ['/locallog/xxx/6897820B-48BC-4B5A-B159-3CAD8438AC92', '/locallog/tmp/90-发布年度停电计划服务-00-SD00053-01-6897820B-48BC-4B5A-B159-3CAD8438AC92'],
                ['/locallog/xxx/9FF974F1-C0DA-492B-9441-67BE7DB25BCB', '/locallog/tmp/91-发布月度停电计划服务-00-SD00054-01-9FF974F1-C0DA-492B-9441-67BE7DB25BCB'],
                ['/locallog/xxx/625978F4-245B-4130-A950-B0EACE067AA6', '/locallog/tmp/92-发布停电申请单-00-SD00050-01-625978F4-245B-4130-A950-B0EACE067AA6'],
                ['/locallog/xxx/617140EF-5D91-4174-BF36-185DB748E2FE', '/locallog/tmp/93-提交客服工单-00-SD00442-617140EF-5D91-4174-BF36-185DB748E2FE'],
                ['/locallog/xxx/A1924F45-8213-46D0-9645-4AA90A0AF4E0', '/locallog/tmp/94-反馈客服工单处理意见-00-SD00077-A1924F45-8213-46D0-9645-4AA90A0AF4E0'],
                ['/locallog/xxx/A4572D56-EFA5-485A-8949-8C760B09DC8D', '/locallog/tmp/95-反馈线损异常处理结果-00-SD00074-A4572D56-EFA5-485A-8949-8C760B09DC8D'],
                ['/locallog/xxx/2729616A-1404-463E-A0A9-34477CA111E4', '/locallog/tmp/96-反馈客户电压质量异常处理结果-00-SD00076-2729616A-1404-463E-A0A9-34477CA111E4'],
                ['/locallog/xxx/93E7EFCA-7856-4288-971E-3CF9BAE75106', '/locallog/tmp/97-反馈工作质量整改情况-00-SD00078-93E7EFCA-7856-4288-971E-3CF9BAE75106'],
                ['/locallog/xxx/2CABD1D2-99FE-405E-9A6D-421360FFB868', '/locallog/tmp/98-提交技术降损需求工单-00-SD00440-2CABD1D2-99FE-405E-9A6D-421360FFB868'],
                ['/locallog/xxx/7AF629C0-F6DC-4DF2-A081-1F2051C99AE0', '/locallog/tmp/99-提交工作质量整改联络单-00-SD00441-7AF629C0-F6DC-4DF2-A081-1F2051C99AE0'],
                ['/locallog/xxx/CA81EC92-2B59-443E-957A-A7F05F1CCFAA', '/locallog/tmp/100-提交客户电压质量异常信息-00-SD00443-CA81EC92-2B59-443E-957A-A7F05F1CCFAA'],
                ['/locallog/xxx/888257ED-C4C2-4E60-9597-531DB158F19D', '/locallog/tmp/101-提交用电安全风险-00-SD00444-888257ED-C4C2-4E60-9597-531DB158F19D'],
                ['/locallog/xxx/DC1CDBC5-2C6A-4BBD-999A-2553DEFE8F7E', '/locallog/tmp/102-反馈用电安全风险处理结果-00-SD00075-DC1CDBC5-2C6A-4BBD-999A-2553DEFE8F7E'],
                ['/locallog/xxx/1DEEB48F-A4F4-4E3D-8D02-6945B49BC163', '/locallog/tmp/103-创建业扩工程电子化移交单服务-00-SD00044-1DEEB48F-A4F4-4E3D-8D02-6945B49BC163'],
                ['/locallog/xxx/AB6D1419-48EF-41EF-A27E-D6D5A22BB130', '/locallog/tmp/104-创建户表资料电子化移交单服务-00-SD00439-AB6D1419-48EF-41EF-A27E-D6D5A22BB130'],
                ['/locallog/xxx/647AF7CD-6074-42DA-AE6E-25E94B67483A', '/locallog/tmp/105-更改电子化移交单服务-00-SD00047-647AF7CD-6074-42DA-AE6E-25E94B67483A'],
                ['/locallog/xxx/93A33BE8-F7EA-440A-9831-D42322B54289', '/locallog/tmp/106-获取营销变压器信息-00-SD01025-93A33BE8-F7EA-440A-9831-D42322B54289'],
                ['/locallog/xxx/00408447-B826-4F72-8B1F-A3F0CCB15982', '/locallog/tmp/107-同步营销对账结果-00-SD00145-00408447-B826-4F72-8B1F-A3F0CCB15982'],
                ['/locallog/xxx/F9DF1DFF-9DBE-4A54-BB9E-A2B35CDA4E8C', '/locallog/tmp/108-同步营销提供应、实收对账表-00-SD00146-F9DF1DFF-9DBE-4A54-BB9E-A2B35CDA4E8C'],
                ['/locallog/xxx/41B09CE0-251F-4D19-8800-608370E1BEC6', '/locallog/tmp/109-提交资金到账信息-00-SD00079-41B09CE0-251F-4D19-8800-608370E1BEC6'],
                ['/locallog/xxx/6A64205E-5A3A-4937-97D6-5D0FCFA64FEF', '/locallog/tmp/110-发送营销财务对账情况表-00-SD01013-6A64205E-5A3A-4937-97D6-5D0FCFA64FEF'],
                ['/locallog/xxx/93E2CF23-5AA6-463D-9E81-7AB18F24FCF4', '/locallog/tmp/111-发送月度实收电费情况报表-00-SD01014-93E2CF23-5AA6-463D-9E81-7AB18F24FCF4'],
                ['/locallog/xxx/80B24DBC-6C3A-45F7-AD43-D7260481615E', '/locallog/tmp/112-同步坏账核销申请信息-00-SD00138-80B24DBC-6C3A-45F7-AD43-D7260481615E'],
                ['/locallog/xxx/B6CD2812-8773-4567-A986-0023EBB2D4B4', '/locallog/tmp/113-反馈坏账核销审核结果-00-SD00082-B6CD2812-8773-4567-A986-0023EBB2D4B4'],
                ['/locallog/xxx/529A7427-33C0-4342-B4B2-0302F6727353', '/locallog/tmp/114-提交购售电预算控制数据-00-SD00084-529A7427-33C0-4342-B4B2-0302F6727353'],
                ['/locallog/xxx/4F453B84-3BED-448A-AC9A-1B0941F34525', '/locallog/tmp/115-接收金融服务评价报表-00-SD01015-4F453B84-3BED-448A-AC9A-1B0941F34525'],
                ['/locallog/xxx/39D4ABD3-16C7-4D7E-A284-913390DABB56', '/locallog/tmp/116-同步交易单位信息-00-SD00140-39D4ABD3-16C7-4D7E-A284-913390DABB56'],
                ['/locallog/xxx/AAC9FF47-F472-4C62-9206-A798B13174D2', '/locallog/tmp/117-同步电厂购电结算单元信息-00-SD00131-AAC9FF47-F472-4C62-9206-A798B13174D2'],
                ['/locallog/xxx/8284C44C-D0B6-40F7-850E-C32B1F0AA4E0', '/locallog/tmp/118-同步网间交易结算单元信息-00-SD00142-8284C44C-D0B6-40F7-850E-C32B1F0AA4E0'],
                ['/locallog/xxx/36B7CD23-A87F-4E01-9844-59B7E9230CF4', '/locallog/tmp/119-同步电力用户应收电费核算数据-00-SD00136-36B7CD23-A87F-4E01-9844-59B7E9230CF4'],
                ['/locallog/xxx/1985C61E-4FF4-4551-B808-F95FCFFC964C', '/locallog/tmp/120-同步自备电厂用户应收核算信息-00-SD00147-1985C61E-4FF4-4551-B808-F95FCFFC964C'],
                ['/locallog/xxx/6F5CA0D2-D120-4DAF-8F52-7294124666B1', '/locallog/tmp/121-同步电厂购电结算信息-00-SD00132-6F5CA0D2-D120-4DAF-8F52-7294124666B1'],
                ['/locallog/xxx/0C0DF16B-15E9-4BF9-8882-2EB6C5888887', '/locallog/tmp/122-同步网间交易结算信息-00-SD00143-0C0DF16B-15E9-4BF9-8882-2EB6C5888887'],
                ['/locallog/xxx/A797F690-0E02-4A84-BB04-7E58DF2D61ED', '/locallog/tmp/123-同步待鉴定减值资产清单信息-00-SD00134-A797F690-0E02-4A84-BB04-7E58DF2D61ED'],
                ['/locallog/xxx/0532939B-7D4D-494C-BD9E-BA85DB40937B', '/locallog/tmp/124-同步电能计量设备报废清单信息-00-SD00137-0532939B-7D4D-494C-BD9E-BA85DB40937B'],
                ['/locallog/xxx/CBB61DD6-5407-4A64-926E-10AA8961D273', '/locallog/tmp/129-同步居民家用电器损坏理赔数据-00-SD00139-CBB61DD6-5407-4A64-926E-10AA8961D273'],
                ['/locallog/xxx/C980F65F-CB5D-4A36-9D79-6C757FCF0FEF', '/locallog/tmp/130-同步电费退费支付信息-00-SD00133-C980F65F-CB5D-4A36-9D79-6C757FCF0FEF'],
                ['/locallog/xxx/0D5C1CD1-86C2-48D1-8ED0-CAE9AC227C63', '/locallog/tmp/131-同步业扩退费支付信息-00-SD00144-0D5C1CD1-86C2-48D1-8ED0-CAE9AC227C63'],
                ['/locallog/xxx/10A8A494-5772-4993-855C-AB6156F28EF1', '/locallog/tmp/132-反馈支付结果-00-SD00081-10A8A494-5772-4993-855C-AB6156F28EF1'],
                ['/locallog/xxx/606F7879-38FA-4DCE-8D8D-EF50D1C6453F', '/locallog/tmp/134-接收教培费用-00-SD00296-606F7879-38FA-4DCE-8D8D-EF50D1C6453F'],
                ['/locallog/xxx/8C431682-5705-425A-915F-C1C59F421799', '/locallog/tmp/137-同步功能数据-00-SD00009-04-8C431682-5705-425A-915F-C1C59F421799'],
                ['/locallog/xxx/1286D79C-2E6B-46C6-8D7C-25701C2C1800', '/locallog/tmp/138-同步业务角色数据-00-SD00005-06-1286D79C-2E6B-46C6-8D7C-25701C2C1800'],
                ['/locallog/xxx/1B301169-0CA2-4C81-8FB6-68B92A93593A', '/locallog/tmp/139-同步业务角色与功能关系数据-00-SD00016-03-1B301169-0CA2-4C81-8FB6-68B92A93593A'],
                ['/locallog/xxx/36D1506F-7896-452E-BD90-5A65C9A33BDD', '/locallog/tmp/141-同步用户与业务角色关系数据-00-SD00011-05-36D1506F-7896-452E-BD90-5A65C9A33BDD'],
                ['/locallog/xxx/EBD15F5A-EFA9-428F-BAD2-5ACF21A6415E', '/locallog/tmp/142-同步用户帐号数据-00-SD00002-07-EBD15F5A-EFA9-428F-BAD2-5ACF21A6415E'],
                ['/locallog/xxx/9AD7F2D5-C439-4138-8FA7-B55ABDA8817D', '/locallog/tmp/143-新增一条员工信息-00-SD00300-9AD7F2D5-C439-4138-8FA7-B55ABDA8817D'],
                ['/locallog/xxx/337B7DF9-C4AB-445E-BCBC-C0AFBF55B46F', '/locallog/tmp/144-更新一条员工信息-00-SD00301-337B7DF9-C4AB-445E-BCBC-C0AFBF55B46F'],
                ['/locallog/xxx/805DF957-65EE-4A82-91E8-1F2AC524F490', '/locallog/tmp/145-删除一条员工信息-00-SD00302-805DF957-65EE-4A82-91E8-1F2AC524F490'],
                ['/locallog/xxx/94D3CBE0-7804-4116-BDC3-05E4A4CE888A', '/locallog/tmp/146-新增一条组织信息-00-SD00297-94D3CBE0-7804-4116-BDC3-05E4A4CE888A'],
                ['/locallog/xxx/1CE30295-6BAE-4842-88C2-EE4D773205A1', '/locallog/tmp/147-更新一条组织信息-00-SD00298-1CE30295-6BAE-4842-88C2-EE4D773205A1'],
                ['/locallog/xxx/5692017B-3C76-4445-B446-85A9600E43D9', '/locallog/tmp/148-删除一条组织信息-00-SD00299-5692017B-3C76-4445-B446-85A9600E43D9'],
                ['/locallog/xxx/9F5CF779-28D8-4C2E-A524-DD22CD769325', '/locallog/tmp/149-新增一条岗位信息-00-SD00303-9F5CF779-28D8-4C2E-A524-DD22CD769325'],
                ['/locallog/xxx/37FDBE40-25F2-41CD-84AE-B7C4B273F544', '/locallog/tmp/150-更新一条岗位信息-00-SD00304-37FDBE40-25F2-41CD-84AE-B7C4B273F544'],
                ['/locallog/xxx/D0DB28DB-EC5F-40E7-8E9D-F3E08A67CE36', '/locallog/tmp/151-删除一条岗位信息-00-SD00305-D0DB28DB-EC5F-40E7-8E9D-F3E08A67CE36']]
    for i in all_file:
        print(i)
        get_files(i[0], i[1], 100)
        print('finish:' + i[1])
