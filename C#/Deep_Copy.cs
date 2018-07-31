namespace DeepCopy {
 class DrawBase: System.Object, ICloneable {
  public List < string > listName = new List < string > ();
  public string name = "old";
  public DrawBase() {}

  public object Clone() {
   //任選一個  
   return this as object; //引用同一個對象  
   //return this.MemberwiseClone(); //淺複製  
   //return new DrawBase() as object;//深複製  
  }
 }


 class Program {
  static void Main(string[] args) {
   DrawBase rect = new DrawBase();
   Console.WriteLine(rect.name);
   DrawBase line = rect.Clone() as DrawBase;
   line.name = "new";
   line.listName.Add("123");
   Console.WriteLine(rect.name);
   Console.WriteLine(rect.listName.Count);
   Console.ReadLine();
  }
 }
 //*/
 public static T Clone < T > (T obj) {
  StringWriter sw = new StringWriter();
  XmlTextWriter tw = null;
  StringReader strReader = null;
  XmlSerializer serializer = null;
  XmlTextReader xmlReader = null;
  //T newObject = null;
  try {
   serializer = new XmlSerializer(obj.GetType());
   tw = new XmlTextWriter(sw);
   serializer.Serialize(tw, obj);
   strReader = new StringReader(sw.ToString());
   serializer = new XmlSerializer(obj.GetType());
   xmlReader = new XmlTextReader(strReader);
   //obj = serializer.Deserialize(xmlReader);
  } catch (Exception ex) {
   //Handle Exception Code
  } finally {
   sw.Close();
   if (tw != null) {
    tw.Close();
   }
  }

  T newObject = (T) serializer.Deserialize(xmlReader);
  return newObject;
 }
 /// <summary>
 /// This way is a few times faster 
 /// than BinarySerialization AND 
 /// this does not require the [Serializable] attribute.
 /// </summary>
 /// <param name="obj"></param>
 /// <returns></returns>
 public static object DeepCopy(object obj) {
  if (obj == null)
   return null;
  Type type = obj.GetType();

  if (type.IsValueType || type == typeof(string)) {
   return obj;
  } else if (type.IsArray) {
   Type elementType = Type.GetType(
    type.FullName.Replace("[]", string.Empty));
   var array = obj as Array;
   Array copied = Array.CreateInstance(elementType, array.Length);
   for (int i = 0; i < array.Length; i++) {
    copied.SetValue(DeepCopy(array.GetValue(i)), i);
   }
   return Convert.ChangeType(copied, obj.GetType());
  } else if (type.IsClass) {

   object toret = Activator.CreateInstance(obj.GetType());
   FieldInfo[] fields = type.GetFields(BindingFlags.Public |
    BindingFlags.NonPublic | BindingFlags.Instance);
   foreach(FieldInfo field in fields) {
    object fieldValue = field.GetValue(obj);
    if (fieldValue == null)
     continue;
    field.SetValue(toret, DeepCopy(fieldValue));
   }

   return toret;
  } else
   throw new ArgumentException("Unknown type");
 }

 public static string GetXMLFromObject(object o) {
  StringWriter sw = new StringWriter();
  XmlTextWriter tw = null;
  try {
   XmlSerializer serializer = new XmlSerializer(o.GetType());
   tw = new XmlTextWriter(sw);
   serializer.Serialize(tw, o);
  } catch (Exception ex) {
   //Handle Exception Code
  } finally {
   sw.Close();
   if (tw != null) {
    tw.Close();
   }
  }
  return sw.ToString();
 }
 public static Object ObjectToXML(string xml, Type objectType) {
  StringReader strReader = null;
  XmlSerializer serializer = null;
  XmlTextReader xmlReader = null;
  Object obj = null;
  try {
   strReader = new StringReader(xml);
   serializer = new XmlSerializer(objectType);
   xmlReader = new XmlTextReader(strReader);
   obj = serializer.Deserialize(xmlReader);
  } catch (Exception exp) {
   //Handle Exception Code
  } finally {
   if (xmlReader != null) {
    xmlReader.Close();
   }
   if (strReader != null) {
    strReader.Close();
   }
  }
  return obj;
 }
/// 此方法有錯誤
 public static object CopyObject(object input) {
  if (input != null) {
   object result = Activator.CreateInstance(input.GetType());
   foreach(FieldInfo field in input.GetType().GetFields(Consts.AppConsts.FullBindingList)) {
    if (field.FieldType.GetInterface("IList", false) == null) {
     field.SetValue(result, field.GetValue(input));
    } else {
     IList listObject = (IList) field.GetValue(result);
     if (listObject != null) {
      foreach(object item in ((IList) field.GetValue(input))) {
       listObject.Add(CopyObject(item));
      }
     }
    }
   }
   return result;
  } else {
   return null;
  }
 }
 /// Clone new results
 //var str = V5.UI.XmlSerializer.GetFormatedXml<MonitorWafersOut[]>(DataOut.ToArray());
 //LastResults = V5.UI.XmlSerializer.GetMessage<MonitorWafersOut[]>(str).ToList();

 //var xml = GetXMLFromObject(DataOut.ToArray());
 //LastResults = (ObjectToXML(xml, typeof(MonitorWafersOut[])) as MonitorWafersOut[]).ToList();

 //LastResults = Clone<MonitorWafersOut[]>(DataOut.ToArray()).ToList();
 LastResults = ((MonitorWafersOut[]) DeepCopy(DataOut.ToArray())).ToList();

 //*/
}