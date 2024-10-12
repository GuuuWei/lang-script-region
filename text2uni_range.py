import re
strlist = "㹴一丁七万丈三上下不与丐丑且丕世丘丙丞丟並丫中丰串丸丹主丼乂乃久么之乍乎乏乒乓乖乘乙乜九乞也乩乳乾亂了予事二于云互亓五井亘亙些亞亟亡亢交亥亦亨享京亭亮亳人什仁仃仄仆仇今介仍仔仕他仗付仙仝仞仟代令以仨仰仲仳仵件价任份仿企伃伉伊伋伍伎伏伐休伕优伙伝伯估伴伶伸伺似伽佃但佇佈位低住佐佑体佔何佗佘余佚佛作佝佞佟你佢佣佩佬佯佰佳併佶佺佻佼佾使侃侄來侈例侍侏侑侔侖侗侘供依侮侯侵侶侷便係促俄俊俋俎俏俐俑俗俘俚保俞俟俠信俣俥俬修俯俱俳俵俶俸俺俾倀倆倉個倌倍倏們倒倔倖倘候倚倜借倡倢倣倥倦倨倩倪倫倬倭值偃假偈偉偌偎偏偕做停健偭偲側偵偶偷偺偽傀傅傌傍傑傖傘備傚傜傢傣催傭傯傲傳傴債傷傻傾僂僅僇僉僎像僑僕僖僚僥僧僩僭僮僱僵價僻儀儂億儆儈儉儐儒儔儕儘償儡優儲儳儷儸儺儻儼儿兀允元兄充兆兇先光克兌免兒兔兕兗党兜兢入內全兩八公六兮共兵其具典兼冀円冇冉冊再冏冑冒冕冗冠冢冤冥冪冬冰冶冷冼冽凃凄准凋凌凍凜凝几凡凭凰凱凳凶凸凹出函刀刁刃分切刈刊刎刑划刖列初判別刨利刪刮到制刷券刺刻剁剃則剉削剋剌前剎剔剖剛剜剝剩剪剮副割剴創剷剽剿劃劄劇劈劉劊劍劑劓力功加劣助努劫劬劭劻劼劾勁勃勇勉勒動勗勘務勛勝勞募勢勣勤勦勰勳勵勸勺勻勾勿包匆匈匍匏匐匕化北匙匝匠匡匣匪匭匯匱匹匾匿區十千卅升午卉半卍卑卒卓協南博卜卞占卡卦卮卯印危即卵卷卸卹卻卿厂厄厘厚厝原厥厭厲去叁參又叉及友双反叔取受叛叟叡叢口古句另叨叩只叫召叭叮可台叱史右叵叶司叻叼吁吃各吆合吉吊吋同名后吏吐向吒吔君吝吞吟吠否吧吩含听吭吮吱吳吵吶吸吹吻吼吽吾呀呂呃呆呈告呎呔呢呣呤呦周呯呱味呵呶呷呸呻呼命呿咀咁咂咄咆咈咋和咎咏咐咒咔咕咖咚咥咦咧咨咩咪咫咬咭咯咱咲咳咸咻咽咾咿哀品哂哄哆哇哈哉哎哏哖哞員哢哥哦哧哨哩哪哭哮哲哺哼哽唁唄唆唇唉唎唏唐唑唔唚唧唬唭售唯唰唱唳唵唷唸唾啁啃啄啅商啊問啐啓啕啖啗啜啞啟啡啣啤啥啦啪啵啶啷啻啼啾喀喂喃善喆喇喉喊喋喎喏喔喘喙喚喜喝喟喧喨喪喫喬單喱喲喳喵喻嗄嗅嗆嗇嗉嗎嗑嗒嗓嗔嗖嗚嗜嗝嗟嗡嗣嗤嗥嗦嗨嗩嗯嗲嗶嗷嗽嗾嘀嘆嘈嘉嘌嘍嘎嘐嘓嘔嘖嘗嘛嘜嘞嘟嘧嘩嘮嘯嘰嘲嘴嘶嘸嘹嘻嘿噁噌噍噎噓噗噘噙噠噢噤噥器噩噪噫噬噯噱噴噶噸噹嚀嚅嚆嚇嚎嚏嚐嚓嚕嚥嚦嚨嚮嚴嚶嚷嚼囀囁囂囈囉囊囌囍囑囓囔囗囚四囝回囟因囡囤囧囪囫囮困囹固囿圃圄圇圈圉國圍園圓圖團圜土圣在圬圭圮圯地圳圻圾址坂均坊坋坌坍坎坏坐坑坔坡坤坦坨坩坪坯坳坵坷坼垂垃型垓垛垠垢垣垮垵埂埃埆埋城埒埔埕埗埜域埠埡埤埭埴埵執培基埼堀堂堃堅堆堇堉堊堝堠堡堤堪堯堰報場堵塊塋塌塑塒塔塗塘塚塞塢填塭塱塵塹塽塾墀境墅墉墊墓墘墜增墟墦墨墩墮墳墻墾壁壅壇壎壑壓壕壘壙壞壟壢壤壩士壬壯壹壺壼壽夏夔夕外夙多夜夠夢夤夥大天太夫夬夭央夯失夷夸夾奀奄奇奈奉奎奏奐契奔奕套奘奚奠奢奧奩奪奭奮女奴奶奸她好妁如妃妄妊妍妏妒妓妖妘妙妝妞妣妤妥妨妮妯妲妳妹妻妾姆姊始姍姐姑姒姓委姘姚姜姝姣姥姦姨姪姬姮姵姻姿威娃娉娌娑娓娘娛娜娟娠娣娥娩娶娼婀婁婆婉婊婕婚婢婦婪婬婭婷婿媒媗媚媛媜媞媧媲媳媼媽媾嫁嫂嫉嫋嫌嫖嫗嫘嫚嫡嫣嫦嫩嫵嫺嫻嬈嬉嬋嬌嬖嬗嬛嬝嬡嬤嬪嬬嬰嬲嬴嬸嬿孀孃孅孌子孑孓孔孕孖字存孚孛孜孝孟孢季孤孥孩孫孬孰孱孳孵學孺孽孿它宅宇守安宋完宏宓宕宗官宙定宛宜客宣室宥宦宮宰害宴宵家宸容宿寂寄寅密寇富寐寒寓寔寞察寡寢寤寥實寧寨審寫寬寮寰寵寶寸寺封射將專尉尊尋對導小少尖尚尢尤尪尬就尷尸尹尺尻尼尾尿局屁屄居屆屈屋屌屍屎屏屐屑展屘屙屜屠屢屣層履屨屬屭屯山屹岈岌岐岑岔岡岩岫岬岭岱岳岷岸峇峋峒峙峨峪峭峯峰峴島峻峽崁崆崇崎崑崔崖崗崙崚崛崢崤崧崩崴崽嵇嵋嵌嵐嵙嵩嵯嶂嶄嶇嶔嶙嶝嶠嶸嶺嶼嶽巉巍巒巔巖川州巡巢工左巧巨巫差己已巳巴巷巽巾巿市布帆希帑帔帕帖帘帙帚帛帝帥師席帳帶帷常帽幀幃幄幅幌幔幕幗幛幟幡幢幣幫干平年并幸幹幻幼幽幾庄庇床序底庖店庚府庠度座庫庭庵庶康庸庹庾廁廂廄廈廉廊廍廓廖廚廝廟廠廡廢廣廨廬廳延廷廸建廾廿弁弄弈弊弋式弒弓弔引弗弘弛弟弦弧弩弭弱弳張強弼彆彈彊彌彎彗彘彙彝彞形彣彤彥彧彩彪彫彬彭彰影彷役彼彿往征待徇很徉徊律後徐徑徒得徘徙徜從徠御徨復循徬徭微徵德徹徼徽心必忌忍忐忑忒忖志忘忙忝忠忡忤忪快忮忱念忸忻忽忿怎怏怒怔怕怖怙怛怜思怠怡急怦性怨怩怪怫怯怵恁恂恃恆恍恐恒恕恙恢恣恤恥恨恩恪恫恬恭息恰恿悄悅悉悌悍悔悖悚悛悟悠患您悱悲悴悵悶悸悻悼悽情惆惇惊惋惑惕惘惚惜惟惠惡惦惰惱想惴惶惹惺惻愀愁愆愈愉愍愎意愕愚愛愜感愣愧愫愴愷愾愿慄慇慈態慌慍慎慓慕慘慚慝慟慢慣慧慨慫慮慰慳慵慶慷慼慾憂憊憋憎憐憑憔憚憤憧憨憩憫憬憮憲憶憾懂懃懇懈應懊懋懌懍懟懣懦懨懲懵懶懷懸懺懼懾懿戀戇戈戊戌戍戎成我戒戕或戚戛戟戡戢截戮戰戲戳戴戶戽戾房所扁扇扈扉手才扎扑扒打扔托扛扞扣扦扭扮扯扱扳扶批扼找承技抄抉把抑抒抓抔投抖抗折抨披抬抱抵抹押抽抿拂拄拆拇拈拉拊拋拌拍拎拏拐拒拓拔拖拗拘拙拚招拜括拭拮拯拱拳拴拷拼拽拾拿持挂指挈按挑挖挨挪挫振挲挹挺挽挾捂捅捆捉捋捌捍捎捏捐捕捧捨捩捫据捱捲捶捷捺捻捽掀掂掃掄授掉掌掏掐排掖掘掙掛掠採探掣接控推掩措掬掮掯掰揀揄揆揉揍描提插揖揚換揠握揣揩揪揭揮援揶揹搆損搏搐搓搔搖搗搜搞搥搧搪搬搭搴搵搶搽搾摀摁摃摑摒摔摘摜摟摧摩摭摯摳摶摸摹摺摻撂撇撈撐撒撓撕撙撚撞撢撣撤撥撩撫撬播撮撰撲撳撻撼撾撿擀擁擂擄擅擇擊擋操擎擒擔擘據擠擢擣擤擦擬擯擰擱擲擴擷擺擻擼擾攀攆攏攔攖攘攙攜攝攢攣攤攥攪攫攬支收攸改攻放政故效敉敏救敔敕敖敗敘教敝敞敢散敦敬敲整敵敷數斂斃文斌斐斑斕斗料斛斜斟斡斤斥斧斫斬斯新斷方於施旁旂旅旋旌旎族旒旖旗既日旦旨早旬旭旱旺旻旼昀昂昃昆昇昉昊昌明昏易昔昕星映昤春昧昨昭是昱昴昵昶晁時晃晉晌晏晒晚晝晞晟晢晤晦晨晬普景晰晴晶晷智晾暄暇暈暉暌暍暐暑暖暗暘暝暢暨暫暮暱暴暸暹曄曆曇曉曖曙曜曝曠曦曩曬曰曲曳更曷書曹曼曾替最會月有朋服朔朕朗望朝期朦朧木未末本札朮朱朴朵机朽杆杈杉杌李杏材村杓杖杙杜杞束杠杪杭杯杰東杲杳杵杷杼松板极枇枉枋析枒枓枕林枚果枝枯枳枴枵架枷枸柁柄柊柏某柑柒染柔柘柙柚柝柞柢查柩柬柯柱柳柴柵柺柿栓栖栗校栢栩株核根格栽桀桁桂桃桄桅框案桉桌桎桐桑桓桔桶桿梁梃梅梆梏梓梔梗梘條梟梠梡梢梧梨梭梯械梱梳梵棄棉棋棍棒棕棗棘棚棟棠棣棧棨森棱棲棵棹棺棻椅椋椌植椎椏椒椪椰椹椽椿楂楊楓楔楚楝楞楠楢楣楨楫業楮極楷楸楹概榆榎榔榕榖榛榜榧榨榫榭榮榴榷榻槁槃構槌槍槐槓槙槤槨槭槲槳槻槽槿樁樂樅樊樑樓標樞樟模樣樨樵樸樹樺樽橄橇橈橋橘橙機橡橢橫橾檀檄檎檐檔檗檜檠檢檣檬檮檯檳檸檻櫂櫃櫓櫚櫛櫝櫞櫟櫥櫨櫪櫫櫬櫸櫺櫻欄欉權欏欒欖欠次欣欲欷欸欺欽款歃歆歇歉歌歎歐歙歛歟歡止正此步武歧歪歲歷歸歹死歿殂殃殄殆殉殊殍殖殘殛殞殤殫殭殮殯殲段殷殺殼殿毀毅毆毋母每毒毓比毗毘毛毫毬毯毽氂氅氈氏氐民氓气氕氖氘氙氚氛氟氡氣氤氦氧氨氪氫氬氮氯氰氳水永氾汀汁求汆汎汐汕汗汙汛汝汞江池污汨汩汪汰汲汴汶決汽汾沁沂沃沅沆沈沉沌沍沏沐沒沓沔沖沙沛沫沬沮沱河沸油治沼沽沾沿況泄泅泉泊泌泓法泖泗泛泠泡波泣泥注泫泮泯泰泱泳泵洁洄洋洌洎洒洗洙洛洞津洨洩洪洫洮洱洲洳洵洶洸活洽派流浙浚浣浥浦浩浪浬浮浯浴海浸浹涂涅涇消涉涌涎涓涔涕涮涯液涵涸涼涿淀淄淅淆淇淋淌淑淒淖淘淙淚淝淞淡淤淦淨淩淪淫淬淮深淳淵混淹淺添淼清渙渚減渝渟渠渡渣渤渥渦温測渭港渲渴游渺渼渾湃湄湊湍湎湔湖湘湛湟湣湧湮湯湲湳溉溏源準溘溚溜溝溟溢溥溪溫溯溱溴溶溺溼滂滄滅滇滉滋滌滎滑滓滔滕滬滯滲滴滷滸滾滿漁漂漆漉漏漓演漕漚漠漢漣漩漪漫漬漯漱漲漳漸漾漿潁潑潔潘潛潟潢潤潦潭潮潯潰潲潸潺潼澀澂澄澆澇澈澍澎澔澗澡澤澦澧澪澱澳澶澹激濁濂濃濕濘濛濟濠濡濤濫濬濮濯濰濱濺濾瀅瀆瀉瀋瀏瀑瀕瀘瀚瀛瀝瀞瀟瀣瀧瀨瀰瀲瀾灌灑灘灝灞灣灤灩火灰灶灸灼災炅炆炊炎炒炔炕炙炤炫炬炭炮炯炳炷炸為烈烊烏烔烘烙烟烤烯烴烷烹烽焉焊焓焗焙焚焜焠無焢焦焯焰焱然焿煆煇煉煊煌煎煒煖煙煜煞煤煥煦照煨煩煬煮煲煸煽熄熊熏熒熔熗熙熟熠熨熬熱熵熹熾燁燃燄燈燉燎燐燒燔燕燙燜營燠燥燦燧燬燭燮燴燻燼燾燿爆爌爍爐爛爨爪爬爭爰爵父爸爹爺爻爽爾爿牆片版牌牒牖牘牙牛牝牟牠牡牢牧物牯牲牴特牽犀犁犄犇犒犖犛犢犧犬犯犰犽狀狂狄狎狐狒狗狙狠狡狩狳狷狸狹狻狼狽猁猊猓猖猙猛猜猝猞猢猥猩猴猶猷猻猾猿獄獅獎獐獒獗獠獨獪獰獲獴獵獷獸獺獻獼獾玀玄玆率玉王玖玟玠玥玦玨玩玫玲玳玷玻珀珂珅珈珉珊珍珞珠珣珥珩珪班珮珺珽現球琅理琇琉琊琍琚琛琢琥琦琨琪琬琮琯琰琲琳琴琵琶琺琿瑀瑁瑄瑋瑕瑗瑙瑚瑛瑜瑞瑟瑠瑢瑣瑤瑩瑪瑭瑯瑰瑱瑳瑾璀璁璃璇璉璋璐璘璜璞璟璣璦璧璨璩環璽璿瓊瓏瓔瓖瓚瓜瓞瓠瓢瓣瓤瓦瓮瓶瓷甄甌甍甕甘甚甜生產甥甦用甩甫甬甭甯田由甲申男甸町甽甾畀畋界畎畏畑畔留畚畜畝畢略畦番畫畯異當畸畿疆疇疊疋疏疑疔疙疚疝疣疤疥疫疱疲疳疵疸疹疼疽疾痀痂病症痊痍痒痔痕痘痙痛痞痠痢痣痤痧痰痱痲痳痴痹痺痼痾痿瘀瘁瘉瘋瘍瘓瘖瘜瘝瘟瘠瘡瘢瘤瘦瘧瘩瘴瘸瘺瘻療癆癇癈癌癒癖癘癟癡癢癤癥癩癬癭癮癰癱癲癸登發白百皂的皆皇皈皋皎皓皖皙皚皤皮皰皴皸皺皿盂盃盅盆盈益盍盎盒盔盛盜盞盟盡監盤盥盧盪目盯盲直相盹盼盾省眇眈眉看眛真眠眥眨眩眯眶眷眸眺眼眾着睇睏睚睛睜睞睡睢督睥睦睨睪睫睬睹睽睿瞄瞅瞇瞋瞌瞎瞑瞞瞟瞠瞥瞧瞪瞬瞭瞰瞳瞻瞼瞽瞿矇矓矗矚矛矜矢矣知矧矩矬短矮矯石矸矽砂砌砍砒研砝砠砥砦砧砭砰砲破砵砷砸硃硅硍硎硐硒硝硫硬确硯硼硿碁碇碉碌碎碑碓碗碘碟碣碧碩碰碳碴確碼碾磁磅磊磋磐磔磕磚磡磧磨磬磯磴磷磺礁礎礑礙礡礦礪礫礬礴示礽社祀祁祂祆祇祈祉祐祓祕祖祗祚祛祝神祟祠祢祥票祭祺祿禁禍禎福禕禚禛禦禧禪禮禰禱禳禹禺禽禾禿秀私秈秉秋科秒秘租秣秤秦秧秩秭移稀稅稈程稍稔稗稚稜稞稟稠種稱稷稹稻稼稽稿穀穆穌積穎穗穠穡穢穩穫穴究穹空穿突窄窈窒窕窖窗窘窟窠窣窩窪窮窯窳窸窺窿竄竅竇竈竊立竑站竟章竣童竦竭端競竹竺竽竿笆笈笏笑笙笛笞笠符笨笪笫第筆等筊筋筌筍筏筐筑筒答策筠筧筮筱筴筵筷箇箋箍箏箔箕算箝箠管箬箭箱箴箸節篁範篆篇築篋篌篙篛篝篠篡篤篦篩篳篷篾簇簋簌簍簑簞簡簣簧簪簫簷簸簽簾簿籀籃籌籍籐籟籠籣籤籥籬籮籲米籽粄粉粑粒粕粗粘粟粥粧粨粩粱粲粳粵粹粼粽精粿糅糊糌糕糖糗糙糜糞糟糠糢糧糬糯糰糴糶糸系糾紀紂約紅紆紇紈紉紊紋納紐紓純紕紗紘紙級紛紜素紡索紫紬紮累細紲紳紹紺紼絀終絃組絆結絕絛絜絝絞絡絢絣給絨絮統絲絳絹綁綉綏綑經綜綞綠綢綣綫綬維綰綱網綴綵綸綹綺綻綽綾綿緇緊緋緒緘緙線緝緞締緡緣編緩緬緯緲練緹緻縈縉縊縐縑縛縝縞縟縣縫縮縱縲縴縵縷縹總績繁繃繅繆繇繈繒織繕繖繙繚繞繡繩繪繫繭繰繳繹繻繼繽繾纂纈續纍纏纓纔纖纘纛纜缶缸缺缽罄罅罈罌罍罐网罔罕罟罡罣罩罪罫置罰署罵罷罹羅羆羈羊羋羌美羔羚羞羡群羥羧羨義羯羰羲羶羸羹羽羿翁翅翊翌翎習翔翕翟翠翡翦翩翫翬翮翰翱翳翹翻翼耀老考耄者耆耋而耍耐耑耒耕耗耘耙耜耦耨耳耶耽耿聆聊聒聖聘聚聞聯聰聱聲聳聵聶職聽聾聿肄肅肆肇肉肋肌肏肓肖肘肚肛肝股肢肥肩肪肫肯肱育肴肺肽胃胄胇背胎胖胗胚胛胜胝胞胡胤胥胭胯胰胱胳胴胸胺胼能脂脅脆脈脊脖脘脛脣脩脫脯脰脹脾腆腈腊腋腌腎腐腑腓腔腕腥腦腩腫腮腰腱腳腴腸腹腺腿膀膂膈膊膏膕膘膚膛膜膝膠膨膩膳膺膻膽膾膿臀臂臃臆臉臊臍臏臘臚臟臠臢臣臥臧臨自臬臭至致臺臻臼臾舀舂舅與興舉舊舌舍舐舒舔舖舘舛舜舞舟舢舨航舫般舵舶舷船舺艇艉艋艏艘艙艦艮良艱色艷艸艾芃芊芋芍芎芒芘芙芛芝芟芡芣芥芩芫芬芭芮芯芰花芳芷芸芹芻芽芾苑苒苓苔苗苙苛苜苞苟苡苣若苦苧苫苯英苳苷苹苺茁茂范茄茅茆茉茗茜茨茫茬茭茯茱茲茴茵茶茸茹茼荀荃荇草荊荏荐荒荔荖荳荷荸荻荼荽莆莉莊莎莒莓莖莘莞莠莢莧莨莩莪莫莽莿菀菁菅菇菈菊菌菓菔菖菘菜菟菠菡菩菫華菰菱菲菴菸菽萁萃萄萇萊萋萌萍萎萘萣萩萬萱萵萸萼落葆葉著葚葛葡董葦葩葫葬葭葯葱葳葵葶葷葺蒂蒐蒔蒙蒜蒞蒟蒡蒨蒯蒲蒴蒸蒹蒺蒻蒼蒽蒿蓀蓁蓄蓆蓉蓊蓋蓍蓑蓓蓖蓪蓬蓮蓴蓼蓽蓿蔆蔑蔓蔔蔗蔘蔚蔡蔣蔥蔦蔫蔬蔭蔻蔽蕁蕃蕈蕉蕊蕎蕙蕞蕤蕨蕩蕪蕭蕾薄薇薈薊薏薑薔薙薛薜薤薦薨薩薪薯薰薹薺藉藍藏藐藕藜藝藤藥藩藪藷藹藺藻藿蘅蘆蘇蘊蘋蘑蘗蘚蘢蘭蘸蘿虎虐虔處虛虜虞號虧虫虯虱虹虺虻蚊蚋蚌蚓蚕蚜蚣蚤蚩蚪蚯蚰蚱蚵蚶蚺蛀蛄蛆蛇蛉蛋蛐蛔蛙蛛蛞蛟蛤蛭蛸蛹蛻蛾蜀蜂蜃蜆蜇蜈蜉蜊蜍蜒蜓蜘蜚蜜蜡蜢蜥蜩蜴蜷蜻蜿蝌蝎蝓蝕蝗蝙蝟蝠蝣蝦蝨蝮蝴蝶蝸螂螃螅螈融螞螟螢螫螭螯螳螺螻螽蟀蟄蟆蟈蟋蟎蟑蟒蟠蟥蟬蟯蟲蟳蟹蟻蟾蠅蠆蠊蠍蠑蠓蠔蠕蠖蠟蠡蠢蠣蠱蠵蠶蠹蠻血衊行衍術衖街衙衛衝衡衢衣表衩衫衰衲衷衹衽衾衿袁袂袈袋袍袒袓袖袞袤袪被袱裁裂裊裎裏裒裔裕裘裙補裝裟裡裨裱裳裴裸裹製褂複褊褐褒褓褔褕褙褚褡褥褪褫褲褶褸褻襁襄襖襞襟襠襤襪襬襯襲西要覃覆覈見規覓視覡覦親覬覲覷覺覽覿觀角觔觚解觥触觴觸言訂訃訇計訊訌討訏訐訓訕訖託記訛訝訟訢訣訥訪設許訴訶診註証訾詁詆詈詎詐詒詔評詛詞詠詡詢詣試詨詩詫詬詭詮詰話該詳詹詼誅誆誇誌認誑誒誓誕誘誚語誠誡誣誤誥誦誧誨說誰課誹誼調諂諄談諉請諍諏諒論諗諛諜諡諢諤諦諧諫諭諮諱諳諶諷諸諺諼諾謀謁謂謄謅謊謎謐謔謖謗謙講謝謠謨謫謬謳謹謾譁證譎譏識譙譚譜譟警譫譬譭譯議譴護譽讀變讎讒讓讖讚讜讞谷谿豁豆豈豉豊豌豎豐豔豕豚象豢豪豫豬豳豸豹豺貂貅貉貊貌貍貓貔貘貝貞負財貢貧貨販貪貫責貯貲貳貴貶買貸費貼貽貿賀賁賂賃賄賅資賈賊賑賒賓賜賞賠賡賢賣賤賦質賬賭賴賸賺賻購賽贅贈贊贍贏贓贔贖贗贛赤赦赧赫赭走赳赴赶起趁超越趕趖趙趟趣趨趯足趴趺趾跆跋跌跎跑跖跚跛距跟跡跤跨跩跪跫路跳跺跼踉踊踏踐踝踞踟踢踩踪踫踭踮踰踱踴踵踹踽蹂蹄蹇蹈蹉蹊蹋蹌蹓蹕蹙蹚蹟蹠蹣蹤蹦蹧蹩蹬蹭蹲蹴蹶蹺蹼躁躂躅躇躉躊躋躍躑躓躕躡躥躪身躬躲躺軀車軋軌軍軏軒軔軛軟軫軸軻軼軾較載輊輒輓輔輕輛輜輝輟輦輩輪輯輳輸輻輾輿轂轄轅轆轉轍轎轔轟轡轤辛辜辟辣辦辨辭辮辯辰辱農辵迂迄迅迆迎近迓返迢迤迥迦迨迪迫迭述迴迷迸迺追退送逃逅逆逍透逐逑途逕逖逗這通逛逝逞速造逡逢連逭逮週進逵逶逸逼逾遁遂遇遊運遍過遏遐遑道達違遘遙遛遜遝遞遠遢遣遨適遭遮遯遲遴遵遶遷選遺遼遽避邀邁邂邃還邇邈邊邋邏邐邑邕邢那邦邨邪邯邰邱邵邶邸郁郃郊郎郗郝郡郢郤部郭郵都郾鄂鄉鄒鄔鄙鄞鄢鄧鄭鄰鄱鄲鄴鄹鄺酆酈酉酊酋酌配酎酐酒酗酚酞酢酣酥酩酪酬酮酯酵酶酷酸酹醂醃醇醉醋醍醐醒醚醛醜醞醣醫醬醮醯醱醴醺釀釁釆采釉釋里重野量釐金釗釘釙釜針釣釦釧釩釭釵釷釹鈇鈉鈍鈎鈐鈑鈔鈕鈞鈣鈦鈴鈷鈸鈹鈺鈽鈾鈿鉀鉅鉈鉉鉋鉍鉑鉗鉚鉛鉞鉤鉦鉬鉸鉻鉼銀銃銅銑銓銖銘銚銜銣銥銦銨銫銬銲銳銷銹銻銼鋁鋃鋅鋇鋌鋏鋐鋒鋤鋦鋪鋯鋰鋸鋼錄錐錒錕錘錙錚錞錠錡錢錦錨錫錮錯錳錵錶錸鍊鍋鍍鍔鍘鍛鍥鍬鍰鍵鍶鍺鍼鍾鎂鎊鎌鎏鎔鎖鎗鎘鎚鎢鎧鎩鎬鎮鎰鎳鎵鏃鏈鏍鏑鏖鏗鏘鏜鏝鏞鏟鏡鏢鏤鏨鏽鐃鐐鐘鐙鐧鐫鐮鐲鐳鐵鐶鐸鐺鑄鑊鑑鑒鑠鑣鑪鑫鑭鑰鑲鑷鑼鑽鑾鑿長門閂閃閉開閎閏閑閒間閔閘閡閣閤閥閨閩閭閱閹閻閾闆闇闈闊闋闌闍闐闔闕闖關闡闢阜阡阨阪阮阱防阻阿陀陂附陋陌降限陘陛陜陝陞陟陡院陣除陪陬陰陲陳陴陵陶陷陸陽隄隅隆隈隊隋隍階隔隕隘隙際障隧隨險隰隱隴隸隹隻隼雀雁雄雅集雇雉雋雌雍雎雒雕雖雙雛雜雞離難雨雩雪雯雰雲零雷雹電需霄霆震霈霉霍霎霏霑霓霖霙霜霞霤霧霪霰露霸霹霽霾靂靄靈青靖靚靛靜非靠靡面靦靨革靳靴靶靼鞅鞋鞍鞏鞘鞠鞣鞦鞭韁韃韆韉韋韌韓韜韭音韶韻響頁頂頃項順頇須頊頌預頑頒頓頗領頜頡頤頫頭頰頷頸頹頻顆題額顎顏顓願顛類顢顥顧顫顯顰顱顳顴風颯颱颳颶颺颼飄飆飛食飢飧飩飪飭飯飲飴飼飽飾餃餅餉養餌餐餒餓餘餚餛餞餡館餬餮餵餽餾餿饃饅饈饉饋饌饑饒饕饗饜饞首馗香馥馨馬馭馮馱馳馴駁駐駑駒駕駙駛駝駟駢駭駱駿騁騎騏騖騙騫騮騰騵騷騾驀驁驃驅驊驍驕驗驚驛驟驢驤驥驪骨骯骰骷骸骼骾髀髁髂髏髑髒髓體髕髖高髡髣髦髫髭髮髯髻鬃鬆鬍鬚鬟鬢鬣鬥鬧鬨鬩鬱鬲鬻鬼魁魂魄魅魍魎魏魑魔魘魚魟魠魩魯魴魷魽鮑鮒鮕鮘鮟鮨鮪鮫鮭鮮鯀鯁鯈鯉鯊鯓鯔鯖鯛鯝鯡鯤鯧鯨鯪鯰鯷鯽鰂鰆鰈鰍鰓鰕鰤鰥鰭鰱鰲鰹鰻鰾鱇鱈鱉鱒鱔鱖鱗鱘鱟鱧鱲鱷鱸鱺鳥鳧鳩鳳鳴鳶鴃鴆鴇鴉鴒鴕鴛鴞鴟鴣鴦鴨鴴鴻鴿鵑鵜鵝鵠鵡鵪鵬鵯鵰鵲鶇鶉鶘鶚鶩鶯鶴鶸鶺鶼鷂鷓鷗鷥鷲鷳鷴鷸鷹鷺鸚鸛鸝鸞鹵鹹鹼鹽鹿麂麋麒麓麗麝麟麥麩麴麵麻麼麾黃黌黍黎黏黐黑黔默黛黜黝點黠黥黨黯黴黷黹黽鼇鼎鼐鼓鼕鼙鼠鼬鼯鼴鼻鼾齁齊齋齒齜齟齡齣齦齧齪齬齲齷龍龐龔龕龜一丁七三下上丈丑丐不丕丙世且丘丞丟丢並丫中串丸凡丹主乃久之尹乍乏乎乒乓乖乘乙九也乞乩乳乾亂了予事二于云井互五亙些亞亟亡交亦亥亨享京亭亮人仁什仃今仄仆仇仍介付仔仕他仗代令仞以仙仿伉伙伊伕伍伐休伏任仼仳仲企件仰份位住佇佗伴佞佛何估佐佑佈伽伺伸佃佔似但佣作你伯低伶余佝佯依併侍佳使佬供例來佰侃侈佩佻侖侏信侵侯便俠俑俏保促侶俚俘俟俊俗侮俐俄係俎俞倌倍倣俯倦倥俸倩倖倆值借倚倒們俺倀倔倨倶倡個候倘俳修倭倪俾倫倉偽停偏假偃偌做偉健偶偎偕偵側倏偷傢傍傅備傑傀傖傘傭債傲傳僅傾催傷傻僧僮僱僥僣僖僚僕像僑億儀僻僵價儂儈儉儐儒儘儔儲優償儡儷儼兀元允兄充光兇兆先克兌兑免兕兔兒兗兜兢入內全兩八六兮公共兵具其典兼冀冉冊再冒 一丁七丈三上下不丐丑且丕世丘丙丞丟丢並丫中串丸丹主乃久之乍乎乏乒乓乖乘乙九乞也乩乳乾亂了予事二于云互五井亙些亞亟亡交亥亦亨享京亭亮人什仁仃仄仆仇今介仍仔仕他仗付仙仞仟代令以仰仲仳件任仼份仿企伉伊伍伏伐休伕伙伯估伴伶伸伺似伽佃但佇佈位低住佐佑佔何佗余佛作佝佞你佣佩佬佯佰佳併佻使侃來侈例侍侏侖供依侮侯侵侶便係促俄俊俎俏俐俑俗俘俚保俞俟俠信修俯俳俸俺俾倀倆倉個倌倍倏們倒倔倖倘候倚借倡倣倥倦倨倩倪倫倭倶值偃假偉偌偎偏偕做停健側偵偶偷偽傀傅傍傑傖傘備傢催傭傲傳債傷傻傾僅像僑僕僖僚僣僥僧僮僱僵價僻儀儂億儈儉儐儒儔儘償儡優儲儷儼兀允元兄充兆兇先光克兌免兑兒兔兕兗兜兢入內全兩八公六兮共兵其具典兼冀冉冊再冑冒冕冠冢冤冥冬冰冶冷冽准凋凌凍凜凝几凡凰凱凳凶凸凹出函刀刁刃分切刈刊刎刑划列初判刨利刪别刮到制刷券刺刻剁剃則削剋剌前剎剔剖剛剜剝剩剪副割剴創剷剽剿劃劇劈劉劍劑力功加劣助努劫劬劾勁勃勇勉勒動勗勘務勛勝勞募勢勤勳勵勸勻勾勿匀包匆匈匍匏匐匕化北匙匝匠匡匣匪匯匱匹匾匿區十千卅升午卉半卑卒卓協南博卜卞占卡卦卧卬卮印危即卵卷卸卹卻卿厄厚原厥厭厲去參又叉及友反叔取受叙叛叟叢口古句另叨叩只叫召叭叮可台叱史右叵司叼吁吃各吆合吉吊吋同名后吏吐向吒君吝吞吟吠否吧吩含吭吮吱吳吵吸吹吻吼吾呀呂呃呆呈告呎呐呢周呱味呵呶呷呸呻呼命咀咄咆咋和咎咐咒咕咖咚咦咧咨咩咪咫咬咯咱咳咸咻咽哀品哂哄哇哈哉哎員哥哦哨哩哪哭哮哲哺哼唁唆唇唉唐唔唧唬售唯唱唳唷唸唾啁啃啄商啊問啕啖啜啞啟啡啣啤啥啦啪啻啼啾喀喂喃善喇喉喊喋喔喘喚喜喝喟喧喪喬單喱喲喳喻嗅嗆嗇嗉嗎嗑嗓嗚嗜嗟嗡嗣嗤嗥嗨嗯嗷嗽嗾嘀嘆嘈嘉嘍嘔嘖嘗嘛嘟嘩嘮嘯嘰嘲嘴嘶嘹嘻嘿噎噓噗噙噢噤噥器噩噪噫噬噯噱噴噸噹嚀嚅嚇嚎嚏嚕嚥嚨嚮嚴嚶嚷嚼囀囁囂囈囉囊囌囑囚四回因囤囪困囱固圃圈國圍園圓圖團土在圬圭圯地圳圾址均坊坍坎坏坐坑坡坤坦坩坪坷坼垂垃型垠垢垣垮埃埋城埔域埠執培基堂堅堆堡堤堪堯堰報場堵塊塌塑塔塗塘塚塞塢填塵塹塾墀境墅墊墓墜增墟墨墮墳墾壁壅壇壑壓壕壘壙壞壟壤壩士壬壯壹壺壽夏夕外夙多夜够夢夤夥大天太夫夭央失夷夸夾奄奇奈奉奎奏奐契奔奕套奘奚奠奢奧奩奪奮女奴奶奸她好如妃妄妊妍妒妓妖妙妝妞妣妤妥妨妮妯妳妹妻妾姆姊始姍姐姑姒姓委姘姚姜姣姥姦姨姪姬姻姿威娃娌娑娓娘娛娜娟娠娣娥娩娶娼婀婁婆婉婊婚婢婦婪婷婿媒媚媛媪媲媳媽媾嫁嫂嫉嫌嫖嫗嫘嫡嫣嫦嫩嫵嫺嫻嬉嬋嬌嬝嬤嬪嬰嬴嬸孀子孑孓孔孕字存孚孜孝孟季孤孩孫孰孱孳孵學孺孽孿宂它宅宇守安宋完宏宗官宙定宛宜客宣室宥宦宮宰害宴宵家容宿寂寄寅密寇富寐寒寓寞察寡寢寤寥實寧寨審寫寬寮寵寶寸寺封射尅將專尉尊尋對導小少尖尚尤尬就尷尸尹尺尼尾尿局屁居屆屈屋屍屎屏屐屑展屜屠屢層履屬屯山屹岌岐岑岔岡岩岫岱岳岷岸峙峨峩峪峭峯峰島峻峽崆崇崎崑崔崖崗崙崛崢崩嵌嵐嵩嶄嶇嶝嶺嶼嶽巍巒巔巖川州巡巢工左巧巨巫差己已巳巴巷巽巾市布帆希帑帕帖帘帚帛帝帥師席帳帶帷常帽幀幅幌幔幕幗幛幟幢幣幫干平年并幸幹幺幻幼幽幾庇序底庖店庚府庠度座庫庭庵庶康庸庾廁廂廈廉廊廓廖廚廝廟廠廢廣廬廳延廷建廿弁弄弈弊式弑弓弔引弗弘弛弟弦弧弩弭弱張強弼彆彈彌彎彗彙彝形彤彥彩彪彫彬彭彰影彷役彼彿往征待徇很徊律後徐徑徒得徘徙從御徨復循徬微徵德徹徽心必忌忍忖志忘忙忝忠快忱念忼忽忿怎怏怒怔怕怖思怠怡急性怨怪怯怱怵恃恆恍恐恕恙恢恣恤恥恨恩恪恫恬恭息恰恿悄悅悉悌悍悔悖悚悟悠患悦您悲悴悵悶悸悻悼悽情惆惋惑惕惘惚惜惟惠惡惦惰惱想惴惶惹惺惻愀愁愈愉愎意愕愚愛愜感愠愣愧愴愾愿慄慇慈態慌慍慎慕慘慚慝慟慢慣慧慨慫慮慰慳慶慷慼慾憂憊憎憐憑憔憚憤憧憩憫憬憲憶憾懂懇懈應懊懍懣懦懲懵懶懷懸懺懼懿戀戈戊戌戍戎成我戒戕或戚戛戟戡戢截戮戰戲戳戴户戾房所扁扇扈扉手才扎扒打扔托扛扣扭扮扯扳扶批扼找承技抄抉把抑抒抓投抖抗折抨披抬抱抵抹押抽抿拂拄拆拇拈拉拋拌拍拐拒拓拔拖拗拘拙拚招拜括拭拮拯拱拳拴拷拼拽拾拿持指挈按挑挖挨挪挫振挺挽挾捂捆捉捎捏捐捕捧捨捩捫捱捲捶捷捻掀掃掄授掉掌掏排掖掘掙掛掠採探掣接控推掩措掬揀揆揉揍描提插揖揚換握揣揩揪揭揮援損搏搓搔搖搗搜搞搪搬搭搶携搽搾摑摒摔摘摟摧摩摯摸摹摺撇撈撐撒撓撕撚撞撤撥撩撫撬播撮撰撲撻撼撿擁擂擄擅擇擊擋操擎擒擔擘據擠擡擦擧擬擰擱擲擴擺擻擾攀攆攏攔攘攙攜攝攣攤攪攫攬支收改攻放政故效敍敏救敖敗敘教敝敞敢散敦敬敲整敵敷數斂斃文斐斑斗料斜斟斡斤斥斧斫斬斯新斷方於施旁旅旋旌旎族旖旗既日旦旨早旬旭旱旺昂昆昇昌明昏易昔星映春昧昨昭是時晃晉晌晏晚晝晤晦晨普景晰晴晶智暇暈暉暑暖暗暢暨暫暮暴暹曆曉曖曙曝曠曦曬曰曲曳更曷書曹曼曾替最會月有朋服朔朕朗望朝期朦朧木未末本札朮朱朴朵朽杆杉李杏材村杖杜杞束杭杯杰東杳杵杷松板枇枉枏析枕林果枝枯枱架枸柄柏某柑染柔柚柜查柩柬柯柱柳柴柵柺柿栓栗校栩株核根格栽桀桂桃桅框案桌桐桑桓桔桶桿梁梃梅梆梓梗條梟梢梧梨梭梯械梳梵棄棉棋棍棒棕棗棘棚棟棠棣棧森棲棵棹棺椅植椎椒椰楊楓楔楚楞楠楨楫業極楷楹概榆榔榕榛榜榦榨榭榮榴榷榻槁構槌槍槐槓槨槳槽樁樂樊樑樓標樞樟模樣樵樸樹樺樽橄橇橋橘橙機橡橢橫檀檄檔檜檢檬檯檳檸檻櫂櫃櫈櫓櫚櫛櫝櫥櫻欄權欖欠次欣欲欺欽款歇歉歌歎歐歟歡止正此步武歧歪歲歷歸歹死歿殃殆殉殊殖殘殤殮殯殲段殷殺殼殿毀毅毆毋母每毒毓比毗毛毫毯毽氊氏氐民氓氖氛氟氣氤氦氧氨氫氮氯氲水永氾汀汁求汐汕汗汝汞江池污汨汪汰汲決汽汾沁沃沅沈沉沌沐沒沖沙沛沫沮沱河沸油治沼沽沾沿況泄泅泉泊泌泓法泗泛泡波泣泥注泰泱泳洋洗洛洞津洩洪洱洲洶活洽派流浙浚浦浩浪浬浮浴海浸涇消涉涌涎涓涕涮涯液涵涸涼淄淅淆淇淋淌淑淒淘淙淚淞淡淤淨淪淫淮深淳淵混淹淺添清渙渚減渝渠渡渣渤渥渦温測渭港渲渴游渺渾湃湊湍湔湖湘湛湧湮湯溉源準溘溜溝溢溥溪溯溶溺溼滂滄滅滇滋滌滑滓滔滬滯滲滴滾滿漁漂漆漏漓演漕漠漢漣漩漪漫漬漱漲漳漸漾漿潑潔潘潛潤潦潭潮潰潸潺潼澀澄澆澈澎澗澡澤澧澱澳澹激濁濂濃濘濛濟濠濡濤濫濬濯濱濺濾瀆瀉瀋瀏瀑瀕瀚瀛瀝瀟瀨瀰瀾灌灑灘灣火灰灶灸灼災炊炎炒炕炙炫炬炭炮炯炳炸為烈烊烏烘烙烟烤烹烽焉焊焙焚無焦焰然煉煌煎煙煜煞煤煥煦照煨煩煬煮煽熄熊熔熙熟熨熬熱熹熾燃燄燈燉燎燐燒燕燙燜營燥燦燧燬燭燮燴燻爆爍爐爛爨爪爬爭爰爲爵父爸爹爺爻爽爾牀牆片版牌牒牖牘牙牛牝牟牠牡牢牧物牯牲牴特牽犀犁犄犒犖犛犢犧犬犯狀狂狄狎狐狗狙狠狡狩狷狸狹狼狽猖猙猛猜猥猩猴猶猷猾猿獄獅獎獐獗獨獰獲獵獷獸獺獻玀玄率玉王玖玟玩玫玲玳玷玻珀珊珍珠班珮現球琅理琉琊琢琥琦琨琪琳琴琶琺琿瑁瑕瑙瑚瑛瑜瑞瑟瑣瑤瑩瑪瑯瑰璃璋璜璣璦璧環璽瓊瓏瓜瓠瓢瓣瓦瓶瓷甄甌甕甘甚甜生產甥甦用甩甫甬甭田由甲申男甸界畏畔留畚畜畝畢略畦畧番畫異當畸疆疇疊疋疎疏疑疙疚疝疤疥疫疲疳疵疹疼疽疾病症痊痔痕痘痙痛痞痢痣痰痱痳痴痺痿瘀瘁瘉瘋瘍瘐瘓瘟瘠瘡瘤瘧瘩瘴瘸療癆癌癒癖癘癡癢癥癩癬癮癱癲癸登發白百皂的皆皇皈皎皓皖皚皮皰皴皺皿盂盃盆盈益盍盎盒盔盛盜盞盟盡監盤盥盧盪目盯盲直相盹盼盾省眉看真眠眨眩眶眷眸眺眼眾着睏睛睜睞睡督睥睦睨睫睬睹睽睾睿瞄瞇瞌瞎瞑瞞瞟瞠瞥瞧瞪瞬瞭瞰瞳瞻瞽瞿矇矓矗矚矛矜矢矣知矩短矮矯石矽砂砌砍研砝砥砧砭砰砲破砸硃硝硫硬硯硼碉碌碎碑碗碘碟碧碩碰碳確碼碾磁磅磊磋磐磕磚磨磬磯磴磷磺礁礎礙礦礪礫礬示社祀祁祆祇祈祉祐祕祖祗祚祝神祟祠祥票祭祺祿禁禍禎福禦禧禪禮禱禺禽禾禿秀私秉秋科秒租秣秤秦秧秩移稀稅稈程稍税稔稚稜稟稠種稱稷稻稼稽稿穀穇穌積穎穗穡穢穩穫穴究穹空穿突窄窈窒窕窖窗窘窟窠窩窪窮窯窺竄竅竇竈竊立站竟章竣童竭端競竹竺竽竿笆笑笙笛笞笠符笨第筆等筋筍筏筐筒答策筠筵筷箋箏箔箕算箝管箭箱箴節篁範篆篇築篙篡篤篩篷篾簇簍簞簡簣簧簪簫簷簸簽簾簿籃籌籍籟籠籤籬籮籲米粉粒粕粗粟粥粱粳粵粺粽精糉糊糕糖糙糜糞糟糠糢糧糯系糾紀紂約紅紇紉紊紋納紐純紕紗紙級紛紜素紡索紫紮累細紳紹紼絀終絃組絆結絕絞絡絢給絨絮統絲絹綁綉綏綑經綜綞綠綢綫維綰綱網綴綵綸綺綻綽綾綿緇緊緒緘線緝緞締緣編緩緬緯練緻縈縑縕縛縣縫縮縱縲縷總績繁繃繅繆織繕繚繞繡繩繪繫繭繳繹繼繽纂續纏纓纖纜缶缸缺缽罄罈罐罔罕罟罩罪置罰署罵罷罹羅羈羊羌美羔羚羞羣群羨義羯羲羶羸羹羽羿翁翅翌翎習翔翕翟翠翡翩翰翱翳翹翺翻翼耀老考者耆而耍耐耒耕耗耘耙耜耳耶耽耿聆聊聖聘聚聞聯聰聱聲聳聶職聽聾聿肄肅肆肇肉肋肌肓肖肘肚肛肝股肢肥肩肪肫肯肱育肴肺胃背胎胖胚胛胞胡胤胥胭胰胱胳胴胸能脂脅脆脈脊脖脣脩脫脯脱脹脾腆腋腎腐腑腔腕腥腦腫腮腰腱腳腸腹腺腿膀膈膊膏膚膛膜膝膠膨膩膳膺膽膾膿臀臂臃臆臉臍臏臘臚臟臣臥臧臨自臭至致臺臻臼臾舀舂舅與興舉舊舌舍舐舒舔舛舜舞舟舢舨航舫般舵舶舷船艇艘艙艦艮良艱色艶艾芋芍芒芙芝芟芥芬芭花芳芹芻芽苑苒苓苔苗苛苞苟苣若苦苧英茁茂范茄茅茉茗茫茱茲茴茵茶茸茹荀荃草荊荏荐荒荔荷荸荻荼莉莊莎莒莓莖莘莞莠莢莫莽菁菅菊菌菜菠菩華菰菱菲菴菸菽萃萄萊萋萌萍萎萬萱萵萸萼落葉著葛葡董葦葩葫葬葱葵葷蒂蒐蒙蒜蒞蒲蒸蒼蒿蓀蓄蓆蓉蓋蓑蓓蓬蓮蔑蔓蔔蔗蔚蔡蔣蔬蔭蔽蕃蕉蕊蕙蕨蕩蕪蕭蕾薄薇薑薔薜薦薩薪薯薰薶藉藍藏藕藝藤藥藩藪藹藺藻蘆蘇蘊蘋蘑蘚蘭蘸蘿虎虐虔處虛虜虞號虧虫虯虱虹蚊蚌蚓蚣蚤蚩蚪蚯蚱蚶蛀蛆蛇蛋蛔蛙蛛蛟蛤蛭蛹蛻蛾蜀蜂蜃蜇蜈蜓蜕蜘蜚蜜蜢蜥蜴蜻蜿蝌蝕蝗蝙蝠蝦蝨蝴蝶蝸螂螃融螞螟螢螫螳螺螻蟀蟆蟈蟋蟑蟒蟬蟯蟲蟻蠅蠍蠏蠔蠕蠟蠡蠢蠣蠱蠶蠹蠻血行衍術街衙衛衝衡衢衣表衫衰衷袁袂袈袋袍袒袖袞被袱裁裂裊裏裔裕裘裙補裝裟裡裨裳裴裸裹製褂複褐褒褓褚褟褥褪褫褲褸褻襃襄襖襟襠襤襪襯襲西要覃覆見規覓視覦親覬覲覺覽觀角解觴觸言訂訃計訊訌討訏訓訕訖託記訛訝訟訣訥訪設許訴診註詁詆詐詔評詛詞詠詢詣試詩詫詬詭詮詰話該詳詹詼誅誇誌認誑誓誕誘語誠誡誣誤誥誦誨說説誰課誼調諂諄談諉請諍諒論諜諦諧諫諭諮諱諷諸諺諾謀謁謂謄謊謎謗謙講謝謠謨謬謹譁證譌譎譏識譚譜警譬譯議譴護譽讀變讒讓讖讚谷谿豁豆豈豉豌豎豐豔豕豚象豢豪豫豬豹豺貂貉貌貍貓貝貞負財貢貧貨販貪貫責貯貲貳貴貶買貸費貼貽貿賀賁賂賃賄賅資賈賊賑賒賓賜賞賠賢賣賤賦質賬賭賴賺購賽贅贈贊贋贍贏贓贖贛赤赦赧赫赭走赳赴起趁超越趕趙趟趣趨足趴趾跆跋跌跎跑跚跛距跟跡跨跪路跳跺跼踏踐踝踟踢踩踪踫踱踴踵踹蹂蹄蹈蹉蹊蹋蹙蹟蹣蹤蹦蹬蹲蹶蹺蹼躁躂躅躇躉躊躍躑躡躪身躬躭躲躺軀車軋軌軍軒軔軛軟軸軻軼軾較載輊輒輓輔輕輛輜輝輟輦輩輪輭輯輸輻輾輿轂轄轅轉轍轎轔轟轡辛辜辟辣辦辨辭辮辯辰辱農迂迄迅迎近返迢迤迥迦迪迫迭述迴迷迸迹迺追退送逃逅逆逍透逐途逕逖逗這通逛逝逞速造逢連逮週進逵逸逼逾遁遂遇遊運遍過遏遐遑道達違遘遙遜遞遠遣遨適遭遮遲遴遵遷選遺遼遽避邀邁邂還邇邊邏邐邑邕邢那邦邨邪邱邵邸郁郊郎郡部郭郵都鄂鄉鄒鄙鄧鄭鄰鄱酉酊酋酌配酒酗酣酥酩酪酬酵酷酸醃醇醉醋醒醜醞醣醫醬醺釀釁采釉釋里重野量釐金釗釘釜針釣釦釧釵鈉鈍鈎鈐鈔鈕鈞鈣鈴鈷鈸鈾鉀鉋鉑鉗鉛鉢鉤銀銅銓銖銘銜銬銳銷銹銻銼鋁鋅鋒鋤鋪鋭鋸鋼錄錐錘錚錠錢錦錨錫錯錳錶鍊鍋鍍鍛鍥鍬鍵鍾鎂鎊鎔鎖鎢鎮鎳鏃鏈鏑鏖鏗鏘鏜鏟鏡鏢鏽鐃鐘鐮鐲鐳鐵鐸鐺鑄鑑鑒鑠鑣鑰鑲鑼鑽鑾鑿長門閂閃閉開閏閑閒間閔閘閡閣閤閥閨閩閭閱閲閻闆闈闊闋闌闐闔闖關闡闢阜阡阪阮阱防阻阿陀附陋陌降限陛陜陡院陣除陪陰陲陳陵陶陷陸陽隅隆隊隋隍階隔隕隘隙際障隧隨險隱隴隸隻雀雁雄雅集雇雉雋雌雍雕雖雙雛雜雞離難雨雪雯雲零雷雹電需霄霆震霉霍霎霏霑霓霖霜霞霧霪露霸霹霽霾靂靄靈青靖靛靜非靠靡面靦靨革靭靴靶靼鞅鞋鞍鞏鞘鞠鞣鞦鞭韁韃韆韋韌韓韜韭音韵韶韻響頁頂頃項順須頌預頑頒頓頗領頡頤頭頰頷頸頹頻顆題額顎顏願顛類顧顫顯顰顱風颯颱颳颶颺颼飄飛食飢飧飩飪飭飯飲飴飼飽飾餃餅餉養餌餐餒餓餘餛餞餡館餵餽餾餿饅饑饒饜饞首香馥馨馬馭馮馱馳馴駁駐駑駒駕駙駛駝駟駢駭駱駿騁騎騖騙騫騰騷騾驀驃驅驕驗驚驛驟驢驥驪骨骯骰骷骸骼髏髒髓體高髦髭髮髯髻鬃鬆鬍鬚鬢鬥鬧鬨鬱鬼魁魂魄魅魏魔魘魚魯魷鮑鮫鮮鯉鯊鯨鯽鰍鰓鰥鰭鰱鰻鰾鱔鱖鱗鱷鱸鳥鳩鳳鳴鳶鴆鴉鴕鴛鴣鴦鴨鴻鴿鵑鵝鵠鵡鵪鵬鵲鶉鶯鶴鷂鷓鷗鷥鷹鷺鸚鸞鹵鹹鹼鹽鹿麋麒麓麗麝麟麥麩麪麴麻麼麽麾黃黍黎黏黑黔默黛黜黝點黠黨黯黴黷鼇鼈鼎鼓鼕鼙鼠鼬鼴鼻鼾齊齋齒齟齡齣齦齪齬齲齷龍龐龔龜冒一丁七丈三上下不丐丑且丕世丘丙丞丟並丫中串丸丹主乃久么之乍乎乏乒乓乖乘乙九乞也乩乳乾亂了予事二于云互五井亙些亞亟亡交亥亦亨享京亭亮人什仁仃仄仆仇今介仍仔仕他仗付仙仞仟代令以仰仲仳件任份仿企伉伊伍伏伐休伕伙伯估伴伶伸伺似伽佃但佇位低住佐佑佔何佗余佛作佝佞你佣佩佬佯佰佳併佻佾使侃來侈例侍侏侖供依侮侯侵侶便係促俄俊俎俏俐俑俗俘俚保俞俟俠信修俯俱俳俸俺俾倀倆倉個倌倍倏們倒倔倖倘候倚借倡倣倥倦倨倩倪倫倭值偃假偉偌偎偏偕做停健側偵偶偷偺偽傀傅傍傑傖傘備傢催傭傯傲傳債傷傻傾僅像僑僕僖僚僥僧僭僮僱僵價僻儀儂億儈儉儐儒儔儘償儡優儲儷儼兀允元兄充兆兇先光克兌免兒兔兕兗兜兢入內全兩八公六兮共兵其具典兼冀冉冊再冑冒冕冗冠冢冤冥冬冰冶冷冽准凋凌凍凜凝几凡凰凱凳凶凸凹出函刀刁刃分切刈刊刎刑划列初判別刨利刪刮到制刷券刺刻剁剃則削剋剌前剎剔剖剛剜剝剩剪副割剴創剷剽剿劃劇劈劉劍劑力功加劣助努劫劬劾勁勃勇勉勒動勗勘務勛勝勞募勢勤勦勵勸勻勾勿包匆匈匍匏匐匕化北匙匝匠匡匣匪匯匱匹匾匿區十千卅升午卉半卑卒卓協南博卜卞占卡卦卮卯印危即卵卷卸卹卻卿厄厚厝原厥厭厲去參又叉及友反叔取受叛叟叢口古句另叨叩只叫召叭叮可台叱史右叵司叼吁吃各吆合吉吊吋同名后吏吐向吒君吝吞吟吠否吧吩含吭吮吱吳吵吶吸吹吻吼吾呀呂呃呆呈告呎呢周呱味呵呶呷呸呻呼命咀咄咆咋和咎咐咒咕咖咚咦咨咪咫咬咯咱咳咸咻咽哀品哂哄哇哈哉哎員哥哦哨哩哪哭哮哲哺哼唁唆唉唐唔唧唬售唯唱唳唷唸唾啃啄商啊問啕啖啜啞啟啡啣啤啦啪啻啼啾喀喂喃善喇喉喊喋喔喘喚喜喝喟喧喪喬單喱喲喳喻嗅嗆嗇嗎嗑嗓嗚嗜嗟嗡嗣嗤嗥嗦嗨嗯嗷嗽嗾嘀嘆嘈嘉嘍嘎嘔嘖嘗嘛嘟嘩嘮嘯嘰嘲嘴嘶嘹嘻嘿噎噓噗噙噢噤噥器噩噪噫噬噯噱噴噸噹嚀嚅嚇嚎嚏嚐嚕嚥嚨嚮嚴嚶嚷嚼囀囁囂囈囉囊囌囑囚四回因囤囪困固圃圈國圍園圓圖團土在圬圭圯地圳圾址均坊坍坎坏坐坑坡坤坦坩坪坷坼垂垃型垠垢垣垮埂埃埋城埔域埠埤執培基堂堅堆堊堡堤堪堯堰報場堵塊塌塑塔塗塘塚塞塢填塭塵塹塾墀境墅墊墓墜增墟墨墮墳墾壁壅壇壑壓壕壘壙壞壟壢壤壩士壬壯壹壺壽夏夔夕外夙多夜夠夢夤夥大天太夫夭央失夷夸夾奄奇奈奉奎奏奐契奔奕套奘奚奠奢奧奩奪奮女奴奶奸她好妁如妃妄妊妍妒妓妖妙妝妞妣妤妥妨妮妯妳妹妻妾姆姊始姍姐姑姒姓委姘姚姜姣姥姦姨姪姬姻姿威娃娌娑娓娘娛娜娟娠娣娥娩娶娼婀婁婆婉婊婚婢婦婪婷婿媒媚媛媲媳媼媽媾嫁嫂嫉嫌嫖嫗嫘嫡嫣嫦嫩嫵嫻嬉嬋嬌嬝嬤嬪嬰嬴嬸孀子孑孓孔孕字存孚孜孝孟季孤孩孫孰孱孳孵學孺孽孿它宅宇守安宋完宏宗官宙定宛宜客宣室宥宦宮宰害宴宵家宸容宿寂寄寅密寇富寐寒寓寞察寡寢寤寥實寧寨審寫寬寮寵寶寸寺封射將專尉尊尋對導小少尖尚尤尬就尷尸尹尺尼尾尿局屁居屆屈屋屍屎屏屐屑展屜屠屢層履屬屯山屹岌岐岑岔岡岩岫岱岳岷岸峙峨峪峭峰島峻峽崁崆崇崎崑崔崖崙崛崢崩嵌嵐嵩嶄嶇嶝嶺嶼嶽巍巒巔巖川州巡巢工左巧巨巫差己已巳巴巷巽巾市布帆希帑帕帖帘帚帛帝帥師席帳帶帷常帽幀幅幌幔幕幗幛幟幢幣幫干平年并幸幹幻幼幽幾庇床序底庖店庚府庠度座庫庭庵庶康庸庾廁廂廈廉廊廓廖廚廝廟廠廢廣廬廳延廷建廿弁弄弈弊式弒弓弔引弗弘弛弟弦弧弩弭弱張強弼彆彈彌彎彗彙彞形彤彥彩彪彫彬彭彰影彷役彼彿往征待徇很徊律後徐徑徒得徘徙從御徨復循徬微徵德徹徽心必忌忍忖志忘忙忝忠快忱念忽忿怎怏怒怔怕怖思怠怡急性怨怪怯怵恃恆恍恐恕恙恢恣恤恥恨恩恪恫恬恭息恰恿悄悅悉悌悍悔悖悚悟悠患您悲悴悵悶悸悻悼悽情惆惋惑惕惘惚惜惟惠惡惦惰惱想惴惶惹惺惻愀愁愈愉愎意愕愚愛愜感愣愧愴愾愿慄慇慈態慌慍慎慕慘慚慝慟慢慣慧慨慫慮慰慶慷慼慾憂憊憎憐憑憔憚憤憧憩憫憬憲憶憾懂懇懈應懊懍懣懦懲懵懶懷懸懺懼懾懿戀戈戊戌戍戎成我戒戕或戚戛戟戡戢截戮戰戲戳戴戶戾房所扁扇扈扉手才扎扒打扔托扛扣扭扮扯扳扶批扼找承技抄抉把抑抒抓投抖抗折抨披抬抱抵抹押抽抿拂拄拆拇拈拉拋拌拍拎拐拒拓拔拖拗拘拙拚招拜括拭拮拯拱拳拴拷拼拽拾拿持指挈按挑挖挨挪挫振挺挽挾捂捆捉捎捏捐捕捧捨捩捫捱捲捶捷捻掀掃掄授掉掌掏排掖掘掙掛掠採探掣接控推掩措掬揀揆揉揍描提插揖揚換握揣揩揪揭揮援損搏搓搔搖搗搜搞搪搬搭搶搽搾摑摒摔摘摟摧摩摯摸摹摺撇撈撐撒撓撕撚撞撤撥撩撫撬播撮撰撲撻撼撿擁擂擄擅擇擊擋操擎擒擔擘據擠擦擬擰擱擲擴擺擻擾攀攆攏攔攘攙攜攝攣攤攪攫攬支收改攻放政故效敏救敖敗敘教敝敞敢散敦敬敲整敵敷數斂斃文斐斑斗料斜斟斡斤斥斧斫斬斯新斷方於施旁旅旋旌旎族旖旗既日旦旨早旬旭旱旺昀昂昆昌明昏易昔星映春昧昨昭是時晃晉晌晏晒晚晝晤晦晨普景晰晴晶智暇暈暉暑暖暗暢暨暫暮暴暹曆曉曖曙曝曠曦曰曲曳更曷書曹曼曾替最會月有朋服朔朕朗望朝期朦朧木未末本札朮朱朴朵朽杉李杏材村杖杜杞束杭杯杰東杳杵杷松板枇枉枋析枕林枚果枝枯枴架枸柄柏某柑染柔柚柞查柩柬柯柱柳柴柵柿栓栗校栩株核根格栽桀桂桃桅框案桌桐桑桓桔桶桿梁梃梅梆梓梔梗條梟梢梧梨梭梯械梱梳梵棄棉棋棍棒棕棗棘棚棟棠棣棧森棲棵棹棺椅植椎椒椰楊楓楔楚楞楠楨楫業極楷楹概榆榔榕榛榜榨榫榭榮榴榷榻槁構槌槍槐槓槨槳槽樁樂樅樊樓標樞樟模樣樵樸樹樺樽橄橇橋橘橙機橡橢橫檀檄檔檜檢檬檳檸檻櫂櫃櫓櫚櫛櫝櫥櫻欄權欖欠次欣欲欺欽款歇歉歌歐歙歟歡止正此步武歧歪歲歷歸歹死歿殃殆殉殊殖殘殤殮殯殲段殷殺殼殿毀毅毆毋母每毒毓比毗毛毫毯毽氏氐民氓氖氛氟氣氤氦氧氨氫氮氯氳水永氾汀汁求汐汕汗汙汝汞江池汨汪汰汲決汽汾沁沃沅沈沉沌沐沒沖沙沛沫沮沱河沸油治沼沽沾沿況泄泅泉泊泌泓法泗泛泡波泣泥注泰泱泳洋洌洗洛洞津洪洱洲洶活洽派流浙浚浦浩浪浬浮浴海浸涇消涉涎涓涕涮涯液涵涸涼淄淅淆淇淋淌淑淒淘淙淚淞淡淤淨淪淫淮深淳淵混淹淺添清渙渚減渝渠渡渣渤渥渦測渭港渲渴游渺渾湃湊湍湔湖湘湛湧湮湯溉源準溘溜溝溢溥溪溫溯溶溺溼滂滄滅滇滋滌滑滓滔滬滯滲滴滾滿漁漂漆漏漓演漕漠漢漣漩漪漫漬漯漱漲漳漸漾漿潑潔潘潛潤潦潭潮潰潸潺潼澀澄澆澈澎澗澡澤澧澱澳澹激濁濂濃濘濛濟濠濡濤濫濬濯濱濺濾瀆瀉瀋瀏瀑瀕瀚瀛瀝瀟瀨瀰瀾灌灑灘灣灤火灰灶灸灼災炊炎炒炕炙炫炬炭炮炯炳炸為烈烊烏烘烙烤烹烽焉焊焙焚無焦焰然煉煌煎煙煜煞煤煥煦照煩煬煮煽熄熊熔熙熟熨熬熱熹熾燃燄燈燉燎燐燒燕燙燜營燥燦燧燬燭燮燴燻爆爍爐爛爨爪爬爭爰爵父爸爹爺爻爽爾牆片版牌牒牖牘牙牛牝牟牠牡牢牧物牯牲牴特牽犀犁犄犒犖犛犢犧犬犯狀狂狄狎狐狗狙狠狡狩狷狸狹狼狽猓猖猙猛猜猥猩猴猶猷猾猿獄獅獎獐獗獨獰獲獵獷獸獺獻玀玄率玉王玖玟玨玩玫玲玳玷玻珀珊珍珠班珮現球琅理琉琊琍琢琥琪琳琴琵琶琺琿瑁瑕瑙瑚瑛瑜瑞瑟瑣瑤瑩瑪瑯瑰璃璋璜璣璦璧璩環璽瓊瓏瓜瓠瓢瓣瓦瓶瓷甄甌甕甘甚甜生產甥甦用甩甫甬甭田由甲申男甸甽界畏畔留畚畜畝畢略畦番畫異當畸疆疇疊疋疏疑疙疚疝疤疥疫疲疳疵疹疼疽疾病症痊痔痕痘痙痛痞痢痣痰痱痲痴痺痿瘀瘁瘉瘋瘍瘓瘟瘠瘡瘤瘦瘧瘩瘴瘸療癆癌癒癖癘癢癥癩癬癮癱癲癸登發白百皂的皆皇皈皎皓皖皚皮皰皴皺皿盂盃盆盈益盍盎盒盔盛盜盞盟盡監盤盥盧盪目盯盲直相盹盼盾省眉看真眠眨眩眶眷眸眺眼眾睏睛睜睞睡督睥睦睨睪睫睬睹睽睿瞄瞇瞌瞎瞑瞞瞟瞠瞥瞧瞪瞬瞭瞰瞳瞻瞽瞿矇矓矗矚矛矜矢矣知矩短矮矯石矽砂砌砍研砝砥砧砭砰破砷砸硃硝硫硬硯硼碉碌碎碑碗碘碟碧碩碰碳確碼碾磁磅磊磋磐磕磚磨磬磯磴磷磺礁礎礙礦礪礫礬示社祀祁祆祇祈祉祐祕祖祗祚祝神祟祠祥票祭祺祿禁禍禎福禦禧禪禮禱禹禽禾禿秀私秉秋科秒租秣秤秦秧秩移稀稅稈程稍稔稚稜稟稠種稱稷稻稼稽稿穀穆穌積穎穗穡穢穩穫穴究穹空穿突窄窈窒窕窖窗窘窟窠窩窪窮窯窺竄竅竇竊立站竟章竣童竭端競竹竺竽竿笆笑笙笛笞笠符笨第筆等筋筍筏筐筒答策筠筵筷箋箏箔箕算箝管箭箱箴節篁範篆篇築篙篛篡篤篩篷篾簇簍簑簞簡簣簧簪簫簷簸簽簾簿籃籌籍籐籟籠籤籬籮籲米粉粒粗粟粥粱粳粵粹粽精糊糕糖糙糜糞糟糠糢糧糯糸系糾紀紂約紅紇紉紊紋納紐純紕紗紙級紛紜素紡索紫紮累細紳紹紼絀終絃組絆結絕絞絡絢給絨絮統絲絹綁綏綑經綜綞綠綢維綰綱網綴綵綸綺綻綽綾綿緇緊緒緘線緝緞締緣編緩緬緯練緻縈縊縑縛縣縫縮縱縲縷總績繁繃繅繆織繕繚繞繡繩繪繫繭繹繼繽纂續纏纓纖纜缶缸缺缽罄罈罐罔罕罟罩罪置罰署罵罷罹羅羈羊羋羌美羔羚羞群羨義羯羲羶羸羹羽羿翁翅翌翎習翔翕翟翠翡翩翰翱翳翹翻翼耀老考者耆而耍耐耒耕耗耘耙耜耳耶耽耿聆聊聖聘聚聞聯聰聱聲聳聶職聽聾聿肄肅肆肇肉肋肌肓肖肘肚肛肝股肢肥肩肪肫肯肱育肴肺胃胄背胎胖胚胛胞胡胤胥胭胰胱胳胴胸能脂脅脆脈脊脖脣脩脫脯脹脾腆腋腎腐腑腔腕腥腦腫腮腰腱腳腸腹腺腿膀膈膊膏膚膛膜膝膠膨膩膳膺膽膾膿臀臂臃臆臉臍臏臘臚臟臣臥臧臨自臬臭至致臺臻臼臾舀舂舅與興舉舊舌舍舐舒舔舛舜舞舟舢舨航舫般舵舶舷船艇艘艙艦艮良艱色艾芋芍芒芙芝芟芥芬芭花芳芹芻芽苑苒苓苔苗苛苜苞苟苣若苦苧英茁茂范茄茅茉茗茫茱茲茴茵茶茸茹荀草荊荏荐荒荔荷荸荻荼莉莊莎莒莓莖莘莞莠莢莫莽菁菅菊菌菜菠菩華菰菱菲菴菸菽萃萄萊萋萌萍萎萬萱萵萸萼落葉著葛葡董葦葩葫葬葵葷蒂蒐蒙蒜蒞蒲蒸蒼蒿蓀蓄蓆蓉蓋蓓蓬蓮蓿蔑蔓蔔蔗蔚蔡蔣蔥蔬蔭蔽蕃蕈蕉蕊蕙蕨蕩蕪蕭蕾薄薇薑薔薛薜薩薪薯薰藉藍藏藐藕藝藤藥藩藪藹藺藻蘆蘇蘊蘋蘑蘗蘚蘭蘸蘿虎虐虔處虛虜虞號虧虫虱虹蚊蚌蚓蚣蚤蚩蚪蚯蚱蚵蚶蛀蛄蛆蛇蛋蛔蛙蛛蛟蛤蛭蛹蛻蛾蜀蜂蜃蜇蜈蜓蜘蜜蜢蜥蜴蜻蜿蝌蝕蝗蝙蝠蝦蝨蝴蝶蝸螂螃融螞螟螢螫螳螺螻蟀蟆蟈蟋蟑蟒蟬蟯蟲蟹蟻蠅蠍蠔蠕蠟蠡蠢蠣蠱蠶蠹蠻血行衍術街衙衛衝衡衢衣表衫衰衷袁袂袈袋袍袒袖袞被袱裁裂裊裔裕裘裙補裝裟裡裨裳裴裸裹製褂複褐褒褓褚褥褪褫褲褶褸褻襄襖襟襠襤襪襯襲西要覃覆見規覓視覦親覬覲覺覽觀角解觴觸言訂訃計訊訌討訐訓訕訖託記訛訝訟訣訥訪設許訴診註証詁詆詐詔評詛詞詠詢詣試詩詫詬詭詮詰話該詳詹詼誅誇誌認誑誓誕誘語誠誡誣誤誥誦誨說誰課誼調諂諄談諉請諍諒論諜諦諧諫諭諮諱諷諸諺諾謀謁謂謄謊謎謗謙講謝謠謨謬謹譁證譎譏識譚譜警譬譯議譴護譽讀變讒讓讖讚谷谿豁豆豈豉豌豎豐豔豕豚象豢豪豫豬豹豺貂貉貊貌貍貓貝貞負財貢貧貨販貪貫責貯貲貳貴貶買貸費貼貽貿賀賁賂賃賄賅資賈賊賑賒賓賜賞賠賢賣賤賦質賬賭賴賺購賽贅贈贊贍贏贓贖贗贛赤赦赧赫赭走赳赴起趁超越趕趙趟趣趨足趴趾跆跋跌跎跑跚跛距跟跡跨跪路跳跺跼踏踐踝踟踢踩踫踱踴踵踹蹂蹄蹈蹉蹊蹋蹙蹣蹤蹦蹬蹲蹶蹺蹼躁躂躅躇躉躊躍躑躡躪身躬躲躺軀車軋軌軍軒軔軛軟軸軻軼軾較載輊輒輓輔輕輛輜輝輟輦輩輪輯輸輻輾輿轂轄轅轉轍轎轔轟轡辛辜辟辣辦辨辭辮辯辰辱農迂迄迅迆迎近返迢迥迦迪迫迭述迴迷迺追退送逃逅逆逍透逐途逕逖逗這通逛逝逞速造逢連逮週進逵逸逼逾遁遂遇遊運遍過遏遐遑道達違遘遙遜遞遠遣遨適遭遮遲遴遵遷選遺遼遽避邀邁邂還邇邊邏邐邑邕邢那邦邪邱邵邸郁郊郎郡部郭郵都鄂鄉鄒鄙鄧鄭鄰鄱鄹酉酊酋酌配酒酗酣酥酩酪酬酵酷酸醃醇醉醋醒醜醞醣醫醬醺釀釁采釉釋里重野量釐金釗釘釜針釣釦釧釵鈉鈍鈐鈔鈕鈞鈣鈴鈷鈸鈽鈾鉀鉋鉑鉗鉛鉤鉸鉻銀銅銓銖銘銜銬銳銷銻銼鋁鋅鋒鋤鋪鋸鋼錄錐錘錚錠錢錦錨錫錯錳錶鍊鍋鍍鍛鍥鍬鍰鍵鍾鎂鎊鎔鎖鎢鎮鎳鏃鏈鏍鏑鏖鏗鏘鏜鏝鏟鏡鏢鏤鏽鐃鐘鐮鐲鐳鐵鐸鐺鑄鑑鑒鑠鑣鑰鑲鑼鑽鑾鑿長門閂閃閉開閏閑閒間閔閘閡閣閤閥閨閩閭閱閻闆闈闊闋闌闐闔闖關闡闢阜阡阪阮阱防阻阿陀附陋陌降限陛陝陡院陣除陪陰陲陳陴陵陶陷陸陽隅隆隊隋隍階隔隕隘隙際障隧隨險隱隴隸隻雀雁雄雅集雇雉雋雌雍雕雖雙雛雜雞離難雨雪雯雲零雷雹電需霄霆震霉霍霎霏霑霓霖霜霞霧霪露霸霹霽霾靂靄靈青靖靛靜非靠靡面靦靨革靴靶靼鞅鞋鞍鞏鞘鞠鞣鞦鞭韁韃韆韋韌韓韜韭音韶韻響頁頂頃項順須頊頌預頑頒頓頗領頡頤頭頰頷頸頹頻顆題額顎顏顓願顛類顧顫顯顰顱風颯颱颳颶颺颼飄飛食飢飧飩飪飭飯飲飴飼飽飾餃餅餉養餌餐餒餓餘餛餞餡館餵餽餾餿饅饑饒饜饞首香馥馨馬馭馮馱馳馴駁駐駑駒駕駙駛駝駟駢駭駱駿騁騎騖騙騫騰騷騾驀驃驅驕驗驚驛驟驢驥驪骨骯骰骷骸骼髏髒髓體高髦髭髮髯髻鬃鬆鬍鬚鬢鬥鬧鬨鬱鬲鬼魁魂魄魅魏魔魘魚魯魷鮑鮪鮫鮮鯉鯊鯧鯨鯽鰍鰓鰥鰭鰱鰻鰾鱉鱔鱖鱗鱷鱸鳥鳩鳳鳴鳶鴆鴉鴒鴕鴛鴣鴦鴨鴻鴿鵑鵝鵠鵡鵪鵬鵲鶉鶯鶴鷂鷓鷗鷥鷹鷺鸚鸞鹹鹼鹽鹿麂麋麒麓麗麝麟麥麩麴麵麻麼麾黃黍黎黏黑黔默黛黜黝點黠黨黯黴黷鼇鼎鼓鼕鼙鼠鼬鼴鼻鼾齊齋齒齜齟齡齣齦齪齬齲齷龍龐龔龜㹴一丁七万丈三上下不与丐丑且丕世丘丙丞丟並丫中丰串丸丹主丼乂乃久么之乍乎乏乒乓乖乘乙乜九乞也乩乳乾亂了予事二于云互亓五井亘亙些亞亟亡亢交亥亦亨享京亭亮亳人什仁仃仄仆仇今介仍仔仕他仗付仙仝仞仟代令以仨仰仲仳仵件价任份仿企伃伉伊伋伍伎伏伐休伕优伙伝伯估伴伶伸伺似伽佃但佇佈位低住佐佑体佔何佗佘余佚佛作佝佞佟你佢佣佩佬佯佰佳併佶佺佻佼佾使侃侄來侈例侍侏侑侔侖侗侘供依侮侯侵侶侷便係促俄俊俋俎俏俐俑俗俘俚保俞俟俠信俣俥俬修俯俱俳俵俶俸俺俾倀倆倉個倌倍倏們倒倔倖倘候倚倜借倡倢倣倥倦倨倩倪倫倬倭值偃假偈偉偌偎偏偕做停健偭偲側偵偶偷偺偽傀傅傌傍傑傖傘備傚傜傢傣催傭傯傲傳傴債傷傻傾僂僅僇僉僎像僑僕僖僚僥僧僩僭僮僱僵價僻儀儂億儆儈儉儐儒儔儕儘償儡優儲儳儷儸儺儻儼儿兀允元兄充兆兇先光克兌免兒兔兕兗党兜兢入內全兩八公六兮共兵其具典兼冀円冇冉冊再冏冑冒冕冗冠冢冤冥冪冬冰冶冷冼冽凃凄准凋凌凍凜凝几凡凭凰凱凳凶凸凹出函刀刁刃分切刈刊刎刑划刖列初判別刨利刪刮到制刷券刺刻剁剃則剉削剋剌前剎剔剖剛剜剝剩剪剮副割剴創剷剽剿劃劄劇劈劉劊劍劑劓力功加劣助努劫劬劭劻劼劾勁勃勇勉勒動勗勘務勛勝勞募勢勣勤勦勰勳勵勸勺勻勾勿包匆匈匍匏匐匕化北匙匝匠匡匣匪匭匯匱匹匾匿區十千卅升午卉半卍卑卒卓協南博卜卞占卡卦卮卯印危即卵卷卸卹卻卿厂厄厘厚厝原厥厭厲去叁參又叉及友双反叔取受叛叟叡叢口古句另叨叩只叫召叭叮可台叱史右叵叶司叻叼吁吃各吆合吉吊吋同名后吏吐向吒吔君吝吞吟吠否吧吩含听吭吮吱吳吵吶吸吹吻吼吽吾呀呂呃呆呈告呎呔呢呣呤呦周呯呱味呵呶呷呸呻呼命呿咀咁咂咄咆咈咋和咎咏咐咒咔咕咖咚咥咦咧咨咩咪咫咬咭咯咱咲咳咸咻咽咾咿哀品哂哄哆哇哈哉哎哏哖哞員哢哥哦哧哨哩哪哭哮哲哺哼哽唁唄唆唇唉唎唏唐唑唔唚唧唬唭售唯唰唱唳唵唷唸唾啁啃啄啅商啊問啐啓啕啖啗啜啞啟啡啣啤啥啦啪啵啶啷啻啼啾喀喂喃善喆喇喉喊喋喎喏喔喘喙喚喜喝喟喧喨喪喫喬單喱喲喳喵喻嗄嗅嗆嗇嗉嗎嗑嗒嗓嗔嗖嗚嗜嗝嗟嗡嗣嗤嗥嗦嗨嗩嗯嗲嗶嗷嗽嗾嘀嘆嘈嘉嘌嘍嘎嘐嘓嘔嘖嘗嘛嘜嘞嘟嘧嘩嘮嘯嘰嘲嘴嘶嘸嘹嘻嘿噁噌噍噎噓噗噘噙噠噢噤噥器噩噪噫噬噯噱噴噶噸噹嚀嚅嚆嚇嚎嚏嚐嚓嚕嚥嚦嚨嚮嚴嚶嚷嚼囀囁囂囈囉囊囌囍囑囓囔囗囚四囝回囟因囡囤囧囪囫囮困囹固囿圃圄圇圈圉國圍園圓圖團圜土圣在圬圭圮圯地圳圻圾址坂均坊坋坌坍坎坏坐坑坔坡坤坦坨坩坪坯坳坵坷坼垂垃型垓垛垠垢垣垮垵埂埃埆埋城埒埔埕埗埜域埠埡埤埭埴埵執培基埼堀堂堃堅堆堇堉堊堝堠堡堤堪堯堰報場堵塊塋塌塑塒塔塗塘塚塞塢填塭塱塵塹塽塾墀境墅墉墊墓墘墜增墟墦墨墩墮墳墻墾壁壅壇壎壑壓壕壘壙壞壟壢壤壩士壬壯壹壺壼壽夏夔夕外夙多夜夠夢夤夥大天太夫夬夭央夯失夷夸夾奀奄奇奈奉奎奏奐契奔奕套奘奚奠奢奧奩奪奭奮女奴奶奸她好妁如妃妄妊妍妏妒妓妖妘妙妝妞妣妤妥妨妮妯妲妳妹妻妾姆姊始姍姐姑姒姓委姘姚姜姝姣姥姦姨姪姬姮姵姻姿威娃娉娌娑娓娘娛娜娟娠娣娥娩娶娼婀婁婆婉婊婕婚婢婦婪婬婭婷婿媒媗媚媛媜媞媧媲媳媼媽媾嫁嫂嫉嫋嫌嫖嫗嫘嫚嫡嫣嫦嫩嫵嫺嫻嬈嬉嬋嬌嬖嬗嬛嬝嬡嬤嬪嬬嬰嬲嬴嬸嬿孀孃孅孌子孑孓孔孕孖字存孚孛孜孝孟孢季孤孥孩孫孬孰孱孳孵學孺孽孿它宅宇守安宋完宏宓宕宗官宙定宛宜客宣室宥宦宮宰害宴宵家宸容宿寂寄寅密寇富寐寒寓寔寞察寡寢寤寥實寧寨審寫寬寮寰寵寶寸寺封射將專尉尊尋對導小少尖尚尢尤尪尬就尷尸尹尺尻尼尾尿局屁屄居屆屈屋屌屍屎屏屐屑展屘屙屜屠屢屣層履屨屬屭屯山屹岈岌岐岑岔岡岩岫岬岭岱岳岷岸峇峋峒峙峨峪峭峯峰峴島峻峽崁崆崇崎崑崔崖崗崙崚崛崢崤崧崩崴崽嵇嵋嵌嵐嵙嵩嵯嶂嶄嶇嶔嶙嶝嶠嶸嶺嶼嶽巉巍巒巔巖川州巡巢工左巧巨巫差己已巳巴巷巽巾巿市布帆希帑帔帕帖帘帙帚帛帝帥師席帳帶帷常帽幀幃幄幅幌幔幕幗幛幟幡幢幣幫干平年并幸幹幻幼幽幾庄庇床序底庖店庚府庠度座庫庭庵庶康庸庹庾廁廂廄廈廉廊廍廓廖廚廝廟廠廡廢廣廨廬廳延廷廸建廾廿弁弄弈弊弋式弒弓弔引弗弘弛弟弦弧弩弭弱弳張強弼彆彈彊彌彎彗彘彙彝彞形彣彤彥彧彩彪彫彬彭彰影彷役彼彿往征待徇很徉徊律後徐徑徒得徘徙徜從徠御徨復循徬徭微徵德徹徼徽心必忌忍忐忑忒忖志忘忙忝忠忡忤忪快忮忱念忸忻忽忿怎怏怒怔怕怖怙怛怜思怠怡急怦性怨怩怪怫怯怵恁恂恃恆恍恐恒恕恙恢恣恤恥恨恩恪恫恬恭息恰恿悄悅悉悌悍悔悖悚悛悟悠患您悱悲悴悵悶悸悻悼悽情惆惇惊惋惑惕惘惚惜惟惠惡惦惰惱想惴惶惹惺惻愀愁愆愈愉愍愎意愕愚愛愜感愣愧愫愴愷愾愿慄慇慈態慌慍慎慓慕慘慚慝慟慢慣慧慨慫慮慰慳慵慶慷慼慾憂憊憋憎憐憑憔憚憤憧憨憩憫憬憮憲憶憾懂懃懇懈應懊懋懌懍懟懣懦懨懲懵懶懷懸懺懼懾懿戀戇戈戊戌戍戎成我戒戕或戚戛戟戡戢截戮戰戲戳戴戶戽戾房所扁扇扈扉手才扎扑扒打扔托扛扞扣扦扭扮扯扱扳扶批扼找承技抄抉把抑抒抓抔投抖抗折抨披抬抱抵抹押抽抿拂拄拆拇拈拉拊拋拌拍拎拏拐拒拓拔拖拗拘拙拚招拜括拭拮拯拱拳拴拷拼拽拾拿持挂指挈按挑挖挨挪挫振挲挹挺挽挾捂捅捆捉捋捌捍捎捏捐捕捧捨捩捫据捱捲捶捷捺捻捽掀掂掃掄授掉掌掏掐排掖掘掙掛掠採探掣接控推掩措掬掮掯掰揀揄揆揉揍描提插揖揚換揠握揣揩揪揭揮援揶揹搆損搏搐搓搔搖搗搜搞搥搧搪搬搭搴搵搶搽搾摀摁摃摑摒摔摘摜摟摧摩摭摯摳摶摸摹摺摻撂撇撈撐撒撓撕撙撚撞撢撣撤撥撩撫撬播撮撰撲撳撻撼撾撿擀擁擂擄擅擇擊擋操擎擒擔擘據擠擢擣擤擦擬擯擰擱擲擴擷擺擻擼擾攀攆攏攔攖攘攙攜攝攢攣攤攥攪攫攬支收攸改攻放政故效敉敏救敔敕敖敗敘教敝敞敢散敦敬敲整敵敷數斂斃文斌斐斑斕斗料斛斜斟斡斤斥斧斫斬斯新斷方於施旁旂旅旋旌旎族旒旖旗既日旦旨早旬旭旱旺旻旼昀昂昃昆昇昉昊昌明昏易昔昕星映昤春昧昨昭是昱昴昵昶晁時晃晉晌晏晒晚晝晞晟晢晤晦晨晬普景晰晴晶晷智晾暄暇暈暉暌暍暐暑暖暗暘暝暢暨暫暮暱暴暸暹曄曆曇曉曖曙曜曝曠曦曩曬曰曲曳更曷書曹曼曾替最會月有朋服朔朕朗望朝期朦朧木未末本札朮朱朴朵机朽杆杈杉杌李杏材村杓杖杙杜杞束杠杪杭杯杰東杲杳杵杷杼松板极枇枉枋析枒枓枕林枚果枝枯枳枴枵架枷枸柁柄柊柏某柑柒染柔柘柙柚柝柞柢查柩柬柯柱柳柴柵柺柿栓栖栗校栢栩株核根格栽桀桁桂桃桄桅框案桉桌桎桐桑桓桔桶桿梁梃梅梆梏梓梔梗梘條梟梠梡梢梧梨梭梯械梱梳梵棄棉棋棍棒棕棗棘棚棟棠棣棧棨森棱棲棵棹棺棻椅椋椌植椎椏椒椪椰椹椽椿楂楊楓楔楚楝楞楠楢楣楨楫業楮極楷楸楹概榆榎榔榕榖榛榜榧榨榫榭榮榴榷榻槁槃構槌槍槐槓槙槤槨槭槲槳槻槽槿樁樂樅樊樑樓標樞樟模樣樨樵樸樹樺樽橄橇橈橋橘橙機橡橢橫橾檀檄檎檐檔檗檜檠檢檣檬檮檯檳檸檻櫂櫃櫓櫚櫛櫝櫞櫟櫥櫨櫪櫫櫬櫸櫺櫻欄欉權欏欒欖欠次欣欲欷欸欺欽款歃歆歇歉歌歎歐歙歛歟歡止正此步武歧歪歲歷歸歹死歿殂殃殄殆殉殊殍殖殘殛殞殤殫殭殮殯殲段殷殺殼殿毀毅毆毋母每毒毓比毗毘毛毫毬毯毽氂氅氈氏氐民氓气氕氖氘氙氚氛氟氡氣氤氦氧氨氪氫氬氮氯氰氳水永氾汀汁求汆汎汐汕汗汙汛汝汞江池污汨汩汪汰汲汴汶決汽汾沁沂沃沅沆沈沉沌沍沏沐沒沓沔沖沙沛沫沬沮沱河沸油治沼沽沾沿況泄泅泉泊泌泓法泖泗泛泠泡波泣泥注泫泮泯泰泱泳泵洁洄洋洌洎洒洗洙洛洞津洨洩洪洫洮洱洲洳洵洶洸活洽派流浙浚浣浥浦浩浪浬浮浯浴海浸浹涂涅涇消涉涌涎涓涔涕涮涯液涵涸涼涿淀淄淅淆淇淋淌淑淒淖淘淙淚淝淞淡淤淦淨淩淪淫淬淮深淳淵混淹淺添淼清渙渚減渝渟渠渡渣渤渥渦温測渭港渲渴游渺渼渾湃湄湊湍湎湔湖湘湛湟湣湧湮湯湲湳溉溏源準溘溚溜溝溟溢溥溪溫溯溱溴溶溺溼滂滄滅滇滉滋滌滎滑滓滔滕滬滯滲滴滷滸滾滿漁漂漆漉漏漓演漕漚漠漢漣漩漪漫漬漯漱漲漳漸漾漿潁潑潔潘潛潟潢潤潦潭潮潯潰潲潸潺潼澀澂澄澆澇澈澍澎澔澗澡澤澦澧澪澱澳澶澹激濁濂濃濕濘濛濟濠濡濤濫濬濮濯濰濱濺濾瀅瀆瀉瀋瀏瀑瀕瀘瀚瀛瀝瀞瀟瀣瀧瀨瀰瀲瀾灌灑灘灝灞灣灤灩火灰灶灸灼災炅炆炊炎炒炔炕炙炤炫炬炭炮炯炳炷炸為烈烊烏烔烘烙烟烤烯烴烷烹烽焉焊焓焗焙焚焜焠無焢焦焯焰焱然焿煆煇煉煊煌煎煒煖煙煜煞煤煥煦照煨煩煬煮煲煸煽熄熊熏熒熔熗熙熟熠熨熬熱熵熹熾燁燃燄燈燉燎燐燒燔燕燙燜營燠燥燦燧燬燭燮燴燻燼燾燿爆爌爍爐爛爨爪爬爭爰爵父爸爹爺爻爽爾爿牆片版牌牒牖牘牙牛牝牟牠牡牢牧物牯牲牴特牽犀犁犄犇犒犖犛犢犧犬犯犰犽狀狂狄狎狐狒狗狙狠狡狩狳狷狸狹狻狼狽猁猊猓猖猙猛猜猝猞猢猥猩猴猶猷猻猾猿獄獅獎獐獒獗獠獨獪獰獲獴獵獷獸獺獻獼獾玀玄玆率玉王玖玟玠玥玦玨玩玫玲玳玷玻珀珂珅珈珉珊珍珞珠珣珥珩珪班珮珺珽現球琅理琇琉琊琍琚琛琢琥琦琨琪琬琮琯琰琲琳琴琵琶琺琿瑀瑁瑄瑋瑕瑗瑙瑚瑛瑜瑞瑟瑠瑢瑣瑤瑩瑪瑭瑯瑰瑱瑳瑾璀璁璃璇璉璋璐璘璜璞璟璣璦璧璨璩環璽璿瓊瓏瓔瓖瓚瓜瓞瓠瓢瓣瓤瓦瓮瓶瓷甄甌甍甕甘甚甜生產甥甦用甩甫甬甭甯田由甲申男甸町甽甾畀畋界畎畏畑畔留畚畜畝畢略畦番畫畯異當畸畿疆疇疊疋疏疑疔疙疚疝疣疤疥疫疱疲疳疵疸疹疼疽疾痀痂病症痊痍痒痔痕痘痙痛痞痠痢痣痤痧痰痱痲痳痴痹痺痼痾痿瘀瘁瘉瘋瘍瘓瘖瘜瘝瘟瘠瘡瘢瘤瘦瘧瘩瘴瘸瘺瘻療癆癇癈癌癒癖癘癟癡癢癤癥癩癬癭癮癰癱癲癸登發白百皂的皆皇皈皋皎皓皖皙皚皤皮皰皴皸皺皿盂盃盅盆盈益盍盎盒盔盛盜盞盟盡監盤盥盧盪目盯盲直相盹盼盾省眇眈眉看眛真眠眥眨眩眯眶眷眸眺眼眾着睇睏睚睛睜睞睡睢督睥睦睨睪睫睬睹睽睿瞄瞅瞇瞋瞌瞎瞑瞞瞟瞠瞥瞧瞪瞬瞭瞰瞳瞻瞼瞽瞿矇矓矗矚矛矜矢矣知矧矩矬短矮矯石矸矽砂砌砍砒研砝砠砥砦砧砭砰砲破砵砷砸硃硅硍硎硐硒硝硫硬确硯硼硿碁碇碉碌碎碑碓碗碘碟碣碧碩碰碳碴確碼碾磁磅磊磋磐磔磕磚磡磧磨磬磯磴磷磺礁礎礑礙礡礦礪礫礬礴示礽社祀祁祂祆祇祈祉祐祓祕祖祗祚祛祝神祟祠祢祥票祭祺祿禁禍禎福禕禚禛禦禧禪禮禰禱禳禹禺禽禾禿秀私秈秉秋科秒秘租秣秤秦秧秩秭移稀稅稈程稍稔稗稚稜稞稟稠種稱稷稹稻稼稽稿穀穆穌積穎穗穠穡穢穩穫穴究穹空穿突窄窈窒窕窖窗窘窟窠窣窩窪窮窯窳窸窺窿竄竅竇竈竊立竑站竟章竣童竦竭端競竹竺竽竿笆笈笏笑笙笛笞笠符笨笪笫第筆等筊筋筌筍筏筐筑筒答策筠筧筮筱筴筵筷箇箋箍箏箔箕算箝箠管箬箭箱箴箸節篁範篆篇築篋篌篙篛篝篠篡篤篦篩篳篷篾簇簋簌簍簑簞簡簣簧簪簫簷簸簽簾簿籀籃籌籍籐籟籠籣籤籥籬籮籲米籽粄粉粑粒粕粗粘粟粥粧粨粩粱粲粳粵粹粼粽精粿糅糊糌糕糖糗糙糜糞糟糠糢糧糬糯糰糴糶糸系糾紀紂約紅紆紇紈紉紊紋納紐紓純紕紗紘紙級紛紜素紡索紫紬紮累細紲紳紹紺紼絀終絃組絆結絕絛絜絝絞絡絢絣給絨絮統絲絳絹綁綉綏綑經綜綞綠綢綣綫綬維綰綱網綴綵綸綹綺綻綽綾綿緇緊緋緒緘緙線緝緞締緡緣編緩緬緯緲練緹緻縈縉縊縐縑縛縝縞縟縣縫縮縱縲縴縵縷縹總績繁繃繅繆繇繈繒織繕繖繙繚繞繡繩繪繫繭繰繳繹繻繼繽繾纂纈續纍纏纓纔纖纘纛纜缶缸缺缽罄罅罈罌罍罐网罔罕罟罡罣罩罪罫置罰署罵罷罹羅羆羈羊羋羌美羔羚羞羡群羥羧羨義羯羰羲羶羸羹羽羿翁翅翊翌翎習翔翕翟翠翡翦翩翫翬翮翰翱翳翹翻翼耀老考耄者耆耋而耍耐耑耒耕耗耘耙耜耦耨耳耶耽耿聆聊聒聖聘聚聞聯聰聱聲聳聵聶職聽聾聿肄肅肆肇肉肋肌肏肓肖肘肚肛肝股肢肥肩肪肫肯肱育肴肺肽胃胄胇背胎胖胗胚胛胜胝胞胡胤胥胭胯胰胱胳胴胸胺胼能脂脅脆脈脊脖脘脛脣脩脫脯脰脹脾腆腈腊腋腌腎腐腑腓腔腕腥腦腩腫腮腰腱腳腴腸腹腺腿膀膂膈膊膏膕膘膚膛膜膝膠膨膩膳膺膻膽膾膿臀臂臃臆臉臊臍臏臘臚臟臠臢臣臥臧臨自臬臭至致臺臻臼臾舀舂舅與興舉舊舌舍舐舒舔舖舘舛舜舞舟舢舨航舫般舵舶舷船舺艇艉艋艏艘艙艦艮良艱色艷艸艾芃芊芋芍芎芒芘芙芛芝芟芡芣芥芩芫芬芭芮芯芰花芳芷芸芹芻芽芾苑苒苓苔苗苙苛苜苞苟苡苣若苦苧苫苯英苳苷苹苺茁茂范茄茅茆茉茗茜茨茫茬茭茯茱茲茴茵茶茸茹茼荀荃荇草荊荏荐荒荔荖荳荷荸荻荼荽莆莉莊莎莒莓莖莘莞莠莢莧莨莩莪莫莽莿菀菁菅菇菈菊菌菓菔菖菘菜菟菠菡菩菫華菰菱菲菴菸菽萁萃萄萇萊萋萌萍萎萘萣萩萬萱萵萸萼落葆葉著葚葛葡董葦葩葫葬葭葯葱葳葵葶葷葺蒂蒐蒔蒙蒜蒞蒟蒡蒨蒯蒲蒴蒸蒹蒺蒻蒼蒽蒿蓀蓁蓄蓆蓉蓊蓋蓍蓑蓓蓖蓪蓬蓮蓴蓼蓽蓿蔆蔑蔓蔔蔗蔘蔚蔡蔣蔥蔦蔫蔬蔭蔻蔽蕁蕃蕈蕉蕊蕎蕙蕞蕤蕨蕩蕪蕭蕾薄薇薈薊薏薑薔薙薛薜薤薦薨薩薪薯薰薹薺藉藍藏藐藕藜藝藤藥藩藪藷藹藺藻藿蘅蘆蘇蘊蘋蘑蘗蘚蘢蘭蘸蘿虎虐虔處虛虜虞號虧虫虯虱虹虺虻蚊蚋蚌蚓蚕蚜蚣蚤蚩蚪蚯蚰蚱蚵蚶蚺蛀蛄蛆蛇蛉蛋蛐蛔蛙蛛蛞蛟蛤蛭蛸蛹蛻蛾蜀蜂蜃蜆蜇蜈蜉蜊蜍蜒蜓蜘蜚蜜蜡蜢蜥蜩蜴蜷蜻蜿蝌蝎蝓蝕蝗蝙蝟蝠蝣蝦蝨蝮蝴蝶蝸螂螃螅螈融螞螟螢螫螭螯螳螺螻螽蟀蟄蟆蟈蟋蟎蟑蟒蟠蟥蟬蟯蟲蟳蟹蟻蟾蠅蠆蠊蠍蠑蠓蠔蠕蠖蠟蠡蠢蠣蠱蠵蠶蠹蠻血衊行衍術衖街衙衛衝衡衢衣表衩衫衰衲衷衹衽衾衿袁袂袈袋袍袒袓袖袞袤袪被袱裁裂裊裎裏裒裔裕裘裙補裝裟裡裨裱裳裴裸裹製褂複褊褐褒褓褔褕褙褚褡褥褪褫褲褶褸褻襁襄襖襞襟襠襤襪襬襯襲西要覃覆覈見規覓視覡覦親覬覲覷覺覽覿觀角觔觚解觥触觴觸言訂訃訇計訊訌討訏訐訓訕訖託記訛訝訟訢訣訥訪設許訴訶診註証訾詁詆詈詎詐詒詔評詛詞詠詡詢詣試詨詩詫詬詭詮詰話該詳詹詼誅誆誇誌認誑誒誓誕誘誚語誠誡誣誤誥誦誧誨說誰課誹誼調諂諄談諉請諍諏諒論諗諛諜諡諢諤諦諧諫諭諮諱諳諶諷諸諺諼諾謀謁謂謄謅謊謎謐謔謖謗謙講謝謠謨謫謬謳謹謾譁證譎譏識譙譚譜譟警譫譬譭譯議譴護譽讀變讎讒讓讖讚讜讞谷谿豁豆豈豉豊豌豎豐豔豕豚象豢豪豫豬豳豸豹豺貂貅貉貊貌貍貓貔貘貝貞負財貢貧貨販貪貫責貯貲貳貴貶買貸費貼貽貿賀賁賂賃賄賅資賈賊賑賒賓賜賞賠賡賢賣賤賦質賬賭賴賸賺賻購賽贅贈贊贍贏贓贔贖贗贛赤赦赧赫赭走赳赴赶起趁超越趕趖趙趟趣趨趯足趴趺趾跆跋跌跎跑跖跚跛距跟跡跤跨跩跪跫路跳跺跼踉踊踏踐踝踞踟踢踩踪踫踭踮踰踱踴踵踹踽蹂蹄蹇蹈蹉蹊蹋蹌蹓蹕蹙蹚蹟蹠蹣蹤蹦蹧蹩蹬蹭蹲蹴蹶蹺蹼躁躂躅躇躉躊躋躍躑躓躕躡躥躪身躬躲躺軀車軋軌軍軏軒軔軛軟軫軸軻軼軾較載輊輒輓輔輕輛輜輝輟輦輩輪輯輳輸輻輾輿轂轄轅轆轉轍轎轔轟轡轤辛辜辟辣辦辨辭辮辯辰辱農辵迂迄迅迆迎近迓返迢迤迥迦迨迪迫迭述迴迷迸迺追退送逃逅逆逍透逐逑途逕逖逗這通逛逝逞速造逡逢連逭逮週進逵逶逸逼逾遁遂遇遊運遍過遏遐遑道達違遘遙遛遜遝遞遠遢遣遨適遭遮遯遲遴遵遶遷選遺遼遽避邀邁邂邃還邇邈邊邋邏邐邑邕邢那邦邨邪邯邰邱邵邶邸郁郃郊郎郗郝郡郢郤部郭郵都郾鄂鄉鄒鄔鄙鄞鄢鄧鄭鄰鄱鄲鄴鄹鄺酆酈酉酊酋酌配酎酐酒酗酚酞酢酣酥酩酪酬酮酯酵酶酷酸酹醂醃醇醉醋醍醐醒醚醛醜醞醣醫醬醮醯醱醴醺釀釁釆采釉釋里重野量釐金釗釘釙釜針釣釦釧釩釭釵釷釹鈇鈉鈍鈎鈐鈑鈔鈕鈞鈣鈦鈴鈷鈸鈹鈺鈽鈾鈿鉀鉅鉈鉉鉋鉍鉑鉗鉚鉛鉞鉤鉦鉬鉸鉻鉼銀銃銅銑銓銖銘銚銜銣銥銦銨銫銬銲銳銷銹銻銼鋁鋃鋅鋇鋌鋏鋐鋒鋤鋦鋪鋯鋰鋸鋼錄錐錒錕錘錙錚錞錠錡錢錦錨錫錮錯錳錵錶錸鍊鍋鍍鍔鍘鍛鍥鍬鍰鍵鍶鍺鍼鍾鎂鎊鎌鎏鎔鎖鎗鎘鎚鎢鎧鎩鎬鎮鎰鎳鎵鏃鏈鏍鏑鏖鏗鏘鏜鏝鏞鏟鏡鏢鏤鏨鏽鐃鐐鐘鐙鐧鐫鐮鐲鐳鐵鐶鐸鐺鑄鑊鑑鑒鑠鑣鑪鑫鑭鑰鑲鑷鑼鑽鑾鑿長門閂閃閉開閎閏閑閒間閔閘閡閣閤閥閨閩閭閱閹閻閾闆闇闈闊闋闌闍闐闔闕闖關闡闢阜阡阨阪阮阱防阻阿陀陂附陋陌降限陘陛陜陝陞陟陡院陣除陪陬陰陲陳陴陵陶陷陸陽隄隅隆隈隊隋隍階隔隕隘隙際障隧隨險隰隱隴隸隹隻隼雀雁雄雅集雇雉雋雌雍雎雒雕雖雙雛雜雞離難雨雩雪雯雰雲零雷雹電需霄霆震霈霉霍霎霏霑霓霖霙霜霞霤霧霪霰露霸霹霽霾靂靄靈青靖靚靛靜非靠靡面靦靨革靳靴靶靼鞅鞋鞍鞏鞘鞠鞣鞦鞭韁韃韆韉韋韌韓韜韭音韶韻響頁頂頃項順頇須頊頌預頑頒頓頗領頜頡頤頫頭頰頷頸頹頻顆題額顎顏顓願顛類顢顥顧顫顯顰顱顳顴風颯颱颳颶颺颼飄飆飛食飢飧飩飪飭飯飲飴飼飽飾餃餅餉養餌餐餒餓餘餚餛餞餡館餬餮餵餽餾餿饃饅饈饉饋饌饑饒饕饗饜饞首馗香馥馨馬馭馮馱馳馴駁駐駑駒駕駙駛駝駟駢駭駱駿騁騎騏騖騙騫騮騰騵騷騾驀驁驃驅驊驍驕驗驚驛驟驢驤驥驪骨骯骰骷骸骼骾髀髁髂髏髑髒髓體髕髖高髡髣髦髫髭髮髯髻鬃鬆鬍鬚鬟鬢鬣鬥鬧鬨鬩鬱鬲鬻鬼魁魂魄魅魍魎魏魑魔魘魚魟魠魩魯魴魷魽鮑鮒鮕鮘鮟鮨鮪鮫鮭鮮鯀鯁鯈鯉鯊鯓鯔鯖鯛鯝鯡鯤鯧鯨鯪鯰鯷鯽鰂鰆鰈鰍鰓鰕鰤鰥鰭鰱鰲鰹鰻鰾鱇鱈鱉鱒鱔鱖鱗鱘鱟鱧鱲鱷鱸鱺鳥鳧鳩鳳鳴鳶鴃鴆鴇鴉鴒鴕鴛鴞鴟鴣鴦鴨鴴鴻鴿鵑鵜鵝鵠鵡鵪鵬鵯鵰鵲鶇鶉鶘鶚鶩鶯鶴鶸鶺鶼鷂鷓鷗鷥鷲鷳鷴鷸鷹鷺鸚鸛鸝鸞鹵鹹鹼鹽鹿麂麋麒麓麗麝麟麥麩麴麵麻麼麾黃黌黍黎黏黐黑黔默黛黜黝點黠黥黨黯黴黷黹黽鼇鼎鼐鼓鼕鼙鼠鼬鼯鼴鼻鼾齁齊齋齒齜齟齡齣齦齧齪齬齲齷龍龐龔龕龜"


ss = [x[0] or x[1] for x in re.findall(r"\{([^}]+)\}|(\S+)", strlist)]
print(ss)

# 去除空格
strlist = strlist.replace(' ', '')

# str 中的每个元素都是一个字符，将其转换为一个整数
cache_list = [ord(c) for c in strlist]

# 压缩
cache_list = list(set(cache_list))
# 排序
cache_list.sort()

remove_list = [123, 125, 9676]
for i in remove_list:
    if i in cache_list:
        cache_list.remove(i)

result = []
start = cache_list[0]
end = cache_list[0]
for i in range(1, len(cache_list)):
    if cache_list[i] - cache_list[i - 1] == 1:
        end = cache_list[i]
    else:
        if start == end:
            result.append([start])
        else:
            result.append([start, end])
        start = cache_list[i]
        end = cache_list[i]
if start == end:
    result.append([start])
else:
    result.append([start, end])
print(result)


# 存为txt文件
with open('uni_range.txt', 'w') as f:
    f.write(str(result))