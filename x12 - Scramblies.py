

'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

def remove(letter,string): #remove a letter from a string, letter assumed to be in string
    first_instance = string.find(letter)
    if first_instance != len(string): # not last letter
        result = string[:first_instance] + string[first_instance+1:]
    else:
        result = string[:len(string)-1]
    return result

def scramble(string1, string2):
    for letter in string2:
        if letter not in string1:
            return False
        if letter in string1:
            string1 = remove(letter,string1)
    return True
'''
# best practice
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
'''


print(scramble('rkqodlw', 'world'))  #true
print(scramble('cedewaraaossoqqyt', 'codewars')) # ==> True
print(scramble('katas', 'steak'))  # ==> False
print(scramble('sandy','ssdan')) # false

'''
passed 444 tests then timed out

Passed: 444 Failed: 0 Exit Code: 1

Test Results:
 Basic tests
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
 Random tests
 Testing for wkolcxyoijf and tzycnvjbdndoe
 Testing for bvtliupbotcjd and pjibbltdouctv
 Testing for gvtbzjeuiigwgq and buqijgezgitgvw
 Testing for wjmzyixhvqshm and einurffxxslvnomyy
 Testing for yzhhxrxromjfxprsmnci and srmxinpxcxryzrjfhmho
 Testing for qxvilprdsozvd and doizrdvplxqvs
 Testing for hxteksnwfxlkobxt and nuxbxpgssvak
 Testing for hhtbrxjkny and xkjntbhryh
 Testing for glkvrzkelsyrztwq and ztlkeqsrzrkylgwv
 Testing for cmhgheooogsrbnmb and osncqxojsrp
 Testing for afwqkfwmdovdnrz and nozqarddwwmfvfk
 Testing for aidekexqdzhwn and xwehikdqzadne
 Testing for aszpvwvsosbjzgk and uccpzbwxscklm
 Testing for pjmejuyqnzdeyzi and owtbbydbxtbb
 Testing for rbbmcjpfjj and bjpfrbjcjm
 Testing for shjrveimhaws and rshhjewsmaiv
 Testing for krbnmsdxeyon and bomsrenydxkn
 Testing for pfnqebjwqisxfc and ygkoyurxmkdqgauttq
 Testing for uccxoikzekgs and zegusikckoxc
 Testing for tczhehlzfdoyevcio and acnyrifqivcmdbyra
 Testing for nyseunqetcd and otgcdatdapeyy
 Testing for zfpdkalgigod and nmngepqctvrlswikcfv
 Testing for onlqfjplntwjq and prxzbfniococ
 Testing for xghnukyepjppjviihha and jhjyuxigpavpinpehhk
 Testing for gpfskjumlrfwvzrpnsmq and rfsuzmnlpwvjfmksgqpr
 Testing for uyuzwnzsfq and zzqswunuyf
 Testing for iwhkdmoderzpti and trddihmwokpeiz
 Testing for acxkeecovpzw and xekzovcwacpe
 Testing for nbmcwaysuvw and bcasvnwyumw
 Testing for svtkniifotimuew and yixadoimwjo
 Testing for tgpxfgjgwcaakzl and evfqmaiqqm
 Testing for iwaxibyabvfdxddjlt and ayxfiwbavddlxidtbj
 Testing for pppnorckjc and olcstgwhywvc
 Testing for iuhjegtilvhne and lutjvhgieihen
 Testing for qsloicwimznyowfx and guppwxduejiaxpzy
 Testing for nfpbzkdhrhs and cdmxnvdqidose
 Testing for gmbcldanivwouxylkg and ocqyryasmtavfz
 Testing for fflbwwssge and gsswbeflwf
 Testing for btksizjsuhzqjcxvzgvn and pvotxuhuau
 Testing for ttuigbmanskyib and juspzxjpopiinstkvsi
 Testing for jujrnuelkmfvahhv and jlvvnkmhuefaurhj
 Testing for wcvgvlfoxsyxsdholpap and slvpposvfagdwoyxlhxc
 Testing for dguskwfttgtz and udsztftgktgw
 Testing for umtimrpzyclrxbdqbucn and qtefacqten
 Testing for kitltdfuuwjhqxmrfzdh and zyuddvvnopnmrnp
 Testing for pnmavivosknarlws and slopvrsnvkmniawa
 Testing for alxiyvismlcwqczki and ebkonqbkzgdkjdcwusff
 Testing for wtsrkstnfroshxv and ntvshtfwksrxsro
 Testing for jhogporrnls and ugxdqvwcquukrvwtbmye
 Testing for drwlcscojtwvf and frjwcodtcwlvs
 Testing for jgmwejhlgm and dvetpxfgniwcmdicagv
 Testing for yygslvrrbkobmseguxdh and klvrrdbegmsbxouhsygy
 Testing for fblxygoadxujybtflf and dfbfgjxatlyfxuolyb
 Testing for uvjvxrsdbnofsvnwvw and egdjygzjixfzbuk
 Testing for xsdalwfpxqlppahxzl and pfpadxxqzlhsaplxlw
 Testing for ncrnmjuqewiwhic and rinwujqniccwemh
 Testing for wiiqvamnolunja and mmusalhsdpgayrk
 Testing for gcneupgiqtamwgwbki and izeuvtrfcmlql
 Testing for yxfctaqxljrtrnpwqr and wmxibesjrbkkanaik
 Testing for mjtkfiiguwfcbisp and betmsqreqfnmjkz
 Testing for ytbqutnvxv and woujivmpuoryat
 Testing for wzpcppggiqwlpwbrav and pigwpplrgcwabwpqvz
 Testing for ixtlzjzajsywklicgqzr and ehsiyuxqlzi
 Testing for xnkywayudglfthmvv and fntzktxshfgcexcvu
 Testing for acvxxgexzoinpcc and bfkcxwbnjfkg
 Testing for yasrubkoqphzmi and hybumpzroisaqk
 Testing for aifnccukaxecmqakrc and rxsfwxfnhwmduoen
 Testing for zyjzedajahdrg and hofmmbeetxszpmvvbbqi
 Testing for nugztsxewxga and tzgbfequymizvcafxmds
 Testing for jzzpesxrvqkew and xmmntquantthlamjk
 Testing for fabwfxskqmuzvesyh and gvgfdegduxfkl
 Testing for tgnlgzalshjjddjze and ljzdltajdgnegjhsz
 Testing for aqblktsvgwxmfgzlwlz and owclrgffqybvgrveug
 Testing for dqawjkalhyyuzgy and yalykyaqudzghjw
 Testing for ckdmhitrvpzaibsb and cbiirapbshmkvtdz
 Testing for uzbapebqzd and rwzgnmloizcacuyvklyf
 Testing for vorqowzbmovc and bhcvajmzuvo
 Testing for miwustwsruxhwkj and aeildqmusfpgnacbplk
 Testing for yzuabxjgezwqhgefe and zfqywjuhezgbeeaxg
 Testing for fqlzzruttmoyksedheyt and tzdyyehttolqrfemzsuk
 Testing for sklodgmsxpisot and olkstimdopsxgs
 Testing for atymohvvdpsagvgoiaxf and pxoagmsvgotiadvyvfah
 Testing for fqvolbemwkqlbvme and ygqbytxhqrxkx
 Testing for uqcsjnyisllzensaqml and frazaxizkhiop
 Testing for yecaqoqwhdpcgq and sfonobetvumqjoyl
 Testing for oddjjlghflvg and lgjdfhdoljgv
 Testing for ptdcvcfoptnvcfvpxqu and copvfvvduccppxtftnq
 Testing for jryxauoybjnspuxwwe and rypeubxanyojuwsjxw
 Testing for wtaiqgwxurihvzzfa and iauiqazrfgtzhwvwx
 Testing for nxgdazmfvxkrnbnscaz and dxmgvfnkxazbazncrsn
 Testing for rhgijkmsuxbrcm and irmcrguhkbjsmx
 Testing for yetwbmqzjjoaabevgitg and bvtjzmbgqiteoyjegwaa
 Testing for ojposaspez and zopssoaepj
 Testing for pxnrkedyocal and xndacyplkreo
 Testing for vbepaxxovsfvcmkdqlrh and xkaewqguuso
 Testing for agpcpvsicrleekrak and yucuedjkuyuhmpkfszh
 Testing for sknahecesnwvufbjlth and ozfwzzvxipjnfyy
 Testing for kscscaervd and rvvlhnugynoeebapenlz
 Testing for wnsyzllulbfv and llyuvzbfsnlw
 Testing for uqoqamydzcqevbyuah and hbyavcezmauoqqyqud
 Testing for ufgdlfrhxwgxncqiundd and mszwjyftcxq
 Testing for oadnywsohr and oahrndowsy
 Testing for xovezfhphjuroqfruat and zcnminmqitg
 Testing for eremwatqfbvx and yhbnrythvwqcaspkrrit
 Testing for vzsheozoxww and zowoxvezshw
 Testing for umjjvlnzktxvjpbryvi and zjryvkijvntmxplvbuj
 Testing for hnqndnmfhexvqiue and endqhfuinhnevqmx
 Testing for qcpydbzxaibqbikmwu and ddjeheyzusojyul
 Testing for wgxfoutcpv and fkgkgeavrkjyrvwj
 Testing for rdbsxvmrsxcbufhyh and sdxrrdrtrdghh
 Testing for pjqdcbgusngiaz and gpszqbganicdju
 Testing for vrnvnjdhhbxbhbzgjn and npiisnbicflbaqjlclsx
 Testing for tnzuggoxyzhgmrlc and hylucgzznrgxtmgo
 Testing for qpolkdhypkqvmcnh and hvqdckpqyohlknmp
 Testing for mtwqldtrriw and etibrwbprdbdunoy
 Testing for cifvmvjpfwle and fkwufryswonervoitihj
 Testing for mgkeivbbmytco and sqmlaiegzhdv
 Testing for fquqwcyvaatt and vawtqcauqtyf
 Testing for ihggsdvjqoiftoak and ikxpyccunfxdrlton
 Testing for fsqkeuwglj and feuskwgljq
 Testing for uutneznljfkqtqps and kjnulnuttpqzsfeq
 Testing for cuwbgwyelyoycduabzlb and fjyohctlwjgsdgowlxj
 Testing for bvaqzivjopfsti and bvqifzjopivsta
 Testing for atfchuffuswrpaag and asfgwctfuaupafrh
 Testing for unfmwwhasjimswu and jauumnsswfmwihw
 Testing for vsdbybjdcl and cbjsyvbddl
 Testing for kxwnaffinsxvsm and xkmwfanxvsfnsi
 Testing for hshkyasyxrlcvbd and oqbfkebxdhqgu
 Testing for wrdlzedpphdxm and xiwtrpdkudepeypsnsbk
 Testing for bqqurvtbzx and ffcrywfeooqfgix
 Testing for eesmbzjaytzoyran and bnmzosrjyeyazeat
 Testing for eclfgmrnfrxz and fgrnlxmfzecr
 Testing for vjrweeqfzo and qpuzqyigxoudme
 Testing for fwojppczbrmdpwgdcrcd and wdzmpcpwcrdfjcgdporb
 Testing for fursqdjhxsbq and ujbqqrsxdfhs
 Testing for fiafdtbnxeaq and dxfsxcrguninqufm
 Testing for pjlxeqdlsodnh and eurreuurrgadlxvrsrdo
 Testing for mvddsqavyukaekqgrcs and ifnvaqkluhaxh
 Testing for ciowpqwrbjv and rxalhsmedrjzbxbe
 Testing for lhnaqkuubihpvw and qvwukhbhnluipa
 Testing for rhbfrbncirrpyg and cnrbfrbrgiryph
 Testing for plkimgulbzgghucrfukt and ucbzrlughtlfgkgiumpk
 Testing for ucqfulmwlkqund and dqwqflmnulucuk
 Testing for emxkcapgrqpozzsupko and jjziaokksgielxy
 Testing for tpxjwfodzkjrj and jzxowjjkdprft
 Testing for navfpwsdvh and awpvfvnshd
 Testing for dtulmczoou and zuuloodtmc
 Testing for ydmdyjoklpohroonrog and odoogrydjrnomklhypo
 Testing for uizjfhemwg and ehmigfwjuz
 Testing for xivyzocymcxnpvxq and qjkzfwwltsl
 Testing for fugqlprayahvmytwsow and vqropyfuamswalghtwy
 Testing for jhwewkhsnyedfx and tgvxxoafeyfqfoykm
 Testing for jukrzzzmran and ioqxkzytrc
 Testing for medbnhgaqnygskss and khfiaatubnpzboymvi
 Testing for rzezekgpyg and eypgzekrgz
 Testing for dhjailrlnmtiftdgwbc and bmfiignlcdwrttahjld
 Testing for whnbpfwcfxt and wnbwxfpchft
 Testing for bcahdwwqoqfhqugvuppc and xaslopdvicvgqlu
 Testing for vpyzaajzrfhtt and zgwtevnyoqvrfjznm
 Testing for xontnsznnmqh and egujzwtnmj
 Testing for xjoovqawrnjxsv and fmzjvluljqlbrqnk
 Testing for uxburtrvrskzs and rkstxurvrszub
 Testing for lvgnlwvwyn and nkcxksnjgtbfl
 Testing for qfmpkdmgfbpmec and xwkomohevqgli
 Testing for kjufavqjqt and btvrxadlngdwlk
 Testing for eunvhjmtphmn and emfkgneanykqoic
 Testing for mrsscmthqrfugkm and rqsmurkmtcfmshg
 Testing for obwwgwquyy and ygwowbyqwu
 Testing for ejxvdrhcxllikbajwli and uvpneewscaix
 Testing for vjyixfklzjlvt and vjyfvlitzljkx
 Testing for jkrubbeojjfspxufvcif and cukfsbxjrifbpjofjuve
 Testing for fuidxvkrljvyweuqo and jbxyhcbbqugkmd
 Testing for eoxqmhvhhihffamrtehb and ggnktidehzyp
 Testing for iwzoxslwznagigwkwjbu and trgxusuxqqijsaa
 Testing for czqqphrbhdjhiyaqt and bqxkhldyclpvyldzt
 Testing for dvuldofeclieavdvhp and fvlvodialpeddchuve
 Testing for zpeorsryxxcmihv and izrscohepxryvmx
 Testing for jhtvzylthxbxgbwzdt and ybxwjxtzdzhhlgtbvt
 Testing for mbyjbiglvzgp and xljevhkohtrzdcohaf
 Testing for wzjtwbohkegtcqxcutxn and mobzcbiaffdvveyaiudw
 Testing for udelucxwsaavgc and byhmxjiejtpeqxyyaa
 Testing for wpxqvoukbapgg and boppaqkgxuvwg
 Testing for rholvoimwiilvhi and zbrkqhsppdmfajzcc
 Testing for oquxxarxrdncfpksna and iqbfagkfirln
 Testing for gicyjlehvtzwnv and byghrwhnpm
 Testing for isxiyevzdialuonefjtx and odzuieevaliyjxfintsx
 Testing for polchbmnsqpyx and jxqwdoqzvmwmu
 Testing for cstssdrusdydddsr and vhiysbkzoeblx
 Testing for kbdvbnvfsbkypxnb and bbykxpsfvbvkdnnb
 Testing for xbnjywnkmkrbxpz and enykconyzicdwb
 Testing for ohkggexfovudzbhbfrd and ratrynhskrlfkqh
 Testing for eomdluhxwexz and oxedmluhewxz
 Testing for jyvdaylduuv and yvuadujyvdl
 Testing for ujanmepbkfa and hdcqpzdiszkyalu
 Testing for qkeuwxbktegnkhk and behtkngxekqwkuk
 Testing for pctwmhwdaik and wwduncngwnrokroxrk
 Testing for wizqbijlebtdwoyaqt and wjqtdbyqeailoiztbw
 Testing for ngozmkqulonjyimu and iwbyjnxpnygwbww
 Testing for aqxanfombkgruqb and uxqmfbqankgorab
 Testing for gouhbhdnuyddh and hhydugohbndud
 Testing for tikzfxrislxrw and mesnufrtbzp
 Testing for rvyeizvntqmdgcrys and vytyvnedmiszqrrgc
 Testing for gahqyzdwxd and xgqzyddwha
 Testing for snjidpkpqynrqrkopjxh and dqjykipkxsrrohpnnqpj
 Testing for mwlccahjlbns and jhmlsclwncab
 Testing for nagiwksronp and evscudxmbvxzg
 Testing for wcilxzurwbmx and cnvayxbxbuxm
 Testing for cuarjdyloxqlgikf and lqfaxdouljrykicg
 Testing for xwxxvqyzdk and wkxxxqdvzy
 Testing for qwxbyfdgqlr and fbltrwkmietpu
 Testing for phizkhufvcf and fihhzkufvpc
 Testing for zhkgptnwmccffe and brhdgiswgzzstbbmt
 Testing for uwxkcpwrcwfvlqjj and dgtpuwfgoww
 Testing for mnejmvtezjksoby and ksoznetvmmbyejj
 Testing for gqkzgltraxxj and tuypuuiadgoykbuy
 Testing for peorohfppfpo and ltdwjkxwiadnztloxd
 Testing for zpcdjihbfdspcnw and fdzhpsbijdcncpw
 Testing for dhrjuivyhbp and vupbdhijhry
 Testing for dhaplghtuzfdwvxcjcr and luhgpctaxrzcjwdhvdf
 Testing for upvbwqpchomcrkbuqrm and tydldljkotkeoesy
 Testing for jyrddhvztoccenbkvh and zdrtcjyohvdckhbvne
 Testing for vttgjqgsfiqszzxbqkh and qvghuqivrmc
 Testing for zvnhpcawdiekkuldj and tgfnmwngbniut
 Testing for mdununbyklepw and ubeuypwknmdnl
 Testing for refbpcwylhsff and pwyfbfschrefl
 Testing for mbisxharnadxl and nirmabxlashxd
 Testing for aylbtednktmpsk and wryiqbfwueqculjym
 Testing for ritfbbyfmredi and qsdxxalxoiiwzq
 Testing for ozngfszvssercfjzw and ukzipgskkaajry
 Testing for dtjtbcgjpmmnxemqz and mzjmbcnxjttepgmdq
 Testing for zkghlvpwzy and yzhvwzkpgl
 Testing for rfddxcgckavwpkb and kwrgvaccdkdpbfx
 Testing for snaczyjhkcizx and brjufgejuw
 Testing for uvtprttsnuzvovmqlquq and hkgbtioqhpq
 Testing for ckkzruxupufljcvtem and kkulfcrujzevcutxpm
 Testing for cftsotelnwrcctbbmum and nuemcbrsobtctfwmctl
 Testing for dttlwdeynttrvmhcqu and xqefaxwfvkomcq
 Testing for xnyhjmulnge and yxmlnngeuhj
 Testing for zunkcujdgver and fnladcwuialhoomf
 Testing for fcjopzsmblginbtjoog and mcawkfmkjftgz
 Testing for ydkodstxlubmqz and btowaatgbsyjobdj
 Testing for ritgrpykzratooems and akgsrrtozropiymet
 Testing for gecmyikppxnrnqdnbf and qgxpyekbnpcmnfrdni
 Testing for hntrgkecercatve and ahwolwuvgtaoctwsf
 Testing for czutgirupxlwgmbuo and fbvpvkhgcaxyx
 Testing for pwotpgjjbtwi and yjzlmoektqthn
 Testing for gvqieckqjixsmlbxj and bgmodayavdouyapnc
 Testing for fwuipkmhxstkwtvi and tkxpwtsuwmhkvfii
 Testing for qkgdtnzcexadny and dcqganydektnzx
 Testing for ycqemvexnbwwcsstqy and semesxwwyqycbntcqv
 Testing for tbuwqohzwsdexeafmyob and oyxaoheusmwbbtdwqfez
 Testing for ijnlpffiqq and yxczwyxdggvd
 Testing for otgiesedux and seotdxeigu
 Testing for xpnoywsdldfwbekrpsd and qjtanwhdflafrx
 Testing for ovtikmvfeuv and aosxyaahpiieffa
 Testing for oexktjdewmuq and ualzbhsrzafibmaard
 Testing for cfgkspsovbehuqjcif and hvjqiuofepfbskcscg
 Testing for zssznsflwlplctcavgs and jrsudtrgiofagejgx
 Testing for ywjfaalrkawsmupwn and suywlrjpawaanwfkm
 Testing for vtqwzinfcwlaxrf and ciaflxwzvnfrwqt
 Testing for qrybohdryjbl and dlykphrnbgt
 Testing for hbqcxdkmqx and xhkbdqmcqx
 Testing for npbxeholuq and pbincpozfbmltjj
 Testing for avahbdfbwudlgp and dplgawvbfadubh
 Testing for hqfexfptgvmp and hmnrlddvrogaxjafik
 Testing for dudansqtahobj and shtqduadjnboa
 Testing for uixtxkducozehbni and rtryfsssgcmyjbnlz
 Testing for jxrbqmhvduscqyugpjcs and hprcsygubqjjvmsuqcdx
 Testing for tuenqgvypyxvpzzhcc and vhtyzhjobzibuc
 Testing for kteqlpmqvpgvktgghflv and plrujtgrrr
 Testing for lcvkuhangeiar and skuzpdflttqbdqukzr
 Testing for suxkykwuwcoktqkwlcyy and kwylkuyxycqwukowsktc
 Testing for uvvxnecuvszrmxod and vxnovmuudvrszexc
 Testing for uivosnrsmhe and exvlrzddgtay
 Testing for tjjyexruwfpoauvnvoe and owxoatvpjnueeurfyvj
 Testing for ckpvuaeccxkireha and huioypmekxyzi
 Testing for qkbxqdgmppurxxdzskwa and axcxvynyejgcz
 Testing for ctbfrxyiyenlr and ylibxtfyrrcne
 Testing for fexexoucomhxpzmqnyni and oxthttljzgpq
 Testing for hsbjeltdffvs and jxsetxazmbmkhxd
 Testing for nbmiqgxvpvocgngmx and nxvnxqogcvmpgigbm
 Testing for whdqoqwbcz and hwbczqdwoq
 Testing for ucmxbzpmylqann and mcxnlzqmnyuapb
 Testing for nrwowlonvefvjgetqcqz and qvoezrcewnnfqtgwojvl
 Testing for jisayojewons and siayeswjojon
 Testing for uvjqoryvkgxpihuffcnz and jwyfgzdloabsiye
 Testing for zyegtzeaqslzerzplf and zzfleetgapyeqzrzls
 Testing for cbrjftxwoaisk and rwcfjkstxabio
 Testing for qcnldkcjglevj and tjnothwikgeem
 Testing for fudlljojdcfkjtc and okhbfygqtpoyg
 Testing for tjifgvzbhhka and ahigzftbjvkh
 Testing for iucavnxcqozaszekuxqc and axqkvuaqzcnccxizesuo
 Testing for mamuiulgerskmpujj and gjkamlmrpiujuseum
 Testing for ooifyjhhzj and qblzscgxnfigs
 Testing for lrlsbarjzgujelteatx and btluegartaxrjlsjelz
 Testing for usuaavaoehbkzs and agcydlsxioj
 Testing for axszfxgqyujeblhcoycx and hycaqyjfoxczsublegxx
 Testing for wipsawcwcqggx and gkrfcxwjsudxgu
 Testing for vsqfyxvdsjszynobzr and rozsvvbjqfzsyxdyns
 Testing for vzvyzccdwstw and vdyvzwstwzcc
 Testing for dwscglylltugsdogfr and esypodfznzubfejlfwp
 Testing for liotggdzhzo and idtghzlgooz
 Testing for lelhlxvajehenya and xgqumhltpdmdtqz
 Testing for fimpwiufjfpzfqqsych and zmxvwbmuoejmu
 Testing for ffotqchbgmahjdlie and iebfttausy
 Testing for aenwsqtprsqg and avyxgrqewlvu
 Testing for mnpijxrsrvlyq and qrpmljrinsvxy
 Testing for tkghmrsdlknoqbb and njscsjnrywtohka
 Testing for kzodrxszqg and qrxogzdskz
 Testing for apozkjwivp and pkovzpaijw
 Testing for wnbzvwntiwscirpz and hbfcqxssbwfpivdalw
 Testing for nydptgqxqfr and zdgnktkugobgpg
 Testing for vunrhigpvweftzwl and dkynuuehmzqgoiiqvcy
 Testing for eceqyhmbjatphdbulhd and quhlbeebacydmhhdjtp
 Testing for ahhmbpairgvdov and bhvohvairapmgd
 Testing for jvkaqlpkeymrechnd and kvrjdlqpheeynmack
 Testing for phrritxrwnjklbfpncny and zcfuuaysnuzy
 Testing for wovyfxxcwegvrk and awrpafgnipdarzjsxjvd
 Testing for yepfhpmabdiv and fowrahxdlah
 Testing for wpizlvfdacgch and zlccvhfwdaigp
 Testing for pyuxblwkrpwemrlvzxf and uxrpkebfmlprwlyvzwx
 Testing for kawfxfwtzphtwljihwyz and tfphwjziltfwwxywkhza
 Testing for suadkfgpinadvpd and iupgvsakpadnddf
 Testing for wolginpbgjqsqvpw and wvpqpqngjobwsgli
 Testing for cngiukiclcnkjruqtb and ihbbhqeykhqfqwidy
 Testing for alklatyjmawtgyhi and ymiywaktaalljhtg
 Testing for bcnvsmetgntsxo and csgmxbevntostn
 Testing for jdjimuypccpxcskr and evvjgtzioiu
 Testing for ypjmeuvqcrdljjitiod and cjaudidmihcjc
 Testing for jothotrwfyyniaeanrem and bsmypwhtiwontwuut
 Testing for vrmxaczcqnpq and qncvaxrcpmqz
 Testing for ijoootxxocxzcnugim and jlupfocqxrzddkznjcc
 Testing for slbyrattrxixfsfq and nqqoqumlrxfyaxvntyf
 Testing for eoakbcbsxxanpwtzbes and addxuhidyzoeojk
 Testing for amokdorkcjts and mscjkdtoarok
 Testing for tgzekgxtcfrzpz and tzepgfzzrcktgx
 Testing for nvrnjwkwcyaveesz and evnnvkwsycrewzja
 Testing for ncblcwnspbbrjzf and zcwbpscjbrlfbnn
 Testing for mkgpoobvrylamkhkt and kkbvhrkptmooaylmg
 Testing for djminrcxvcrvrpasbywr and wyivjxrccrnadpvrrmsb
 Testing for fidfcrfzdchargf and mknhhjvryxzna
 Testing for ihvlrwugbn and nhwvbgluri
 Testing for dayzzhxwscvgfsxkjmz and kszydxjzhxfvcgzwsam
 Testing for ydwklayznzdzqjq and okvtjakqdpsjbz
 Testing for nrvmfpbttysvqnngnnz and udvjcgfvqehtdacdhead
 Testing for obcmizufgvgxkccfmuj and jcvcixomffzucbgmukg
 Testing for mfpmpfahivt and cjagzlzpzynymlhpbp
 Testing for njwnpfrewpamhxgx and nnewcanahyatwlx
 Testing for csljwtzmcypymmtnvobz and btauqobffphuvjvx
 Testing for gguawitsanpqvkmibmz and djyhydadrvked
 Testing for efndfswifdnvp and sfidnefdpvnwf
 Testing for xrkufwqdxuajrvixdxn and ijrndqxarxdvfxxkuuw
 Testing for sovroedkkpbhnx and rkokhpxnvosdeb
 Testing for djvnievmdczyzxznwcv and xmdkipjievgqmwlv
 Testing for ojzgwahsdfeanadq and qaawsfjdzandeohg
 Testing for bquzpreotsazr and baqoptrzreusz
 Testing for xqqaopxnpsbpddsalcwk and zmshmpwtljicyz
 Testing for vsvvtbstilvvhfiwg and vifhtstlgivsbvvwv
 Testing for aobtjchfemloyrbxyte and tjpdctfkwmriudmtvtx
 Testing for gedbcljmgvzqzohwp and ifbyhuuavek
 Testing for snqvfbbngqdrogkfagvb and fjadimxvwkmgc
 Testing for oxridtkesvlchau and xdthrkilocasvue
 Testing for zihxehhsaayps and wpdfllfilvkep
 Testing for qcibpwxhgjekg and romltsonyppo
 Testing for cawfqqwcqrukiysdlzxc and lrkkecbyvrsdlfptcegy
 Testing for rsofxcquubgwn and ocsfquxwrgnub
 Testing for rnwdjnvfjt and bwfmkxrahyymu
 Testing for majnqbtqvss and jnbqvsmtqas
 Testing for lgjqflggjpkdrsi and jldksjfgprgqigl
 Testing for itvtkkpllraamxfs and ttlfophkaqdbk
 Testing for fstooiidfbamofhw and fowatfodbiismohf
 Testing for uaydxgjnmviglbpdfqln and mkftplsvnbamgmmechx
 Testing for vvytxjqyibcg and vixyjtycgvqb
 Testing for vxyvfntftbvkuo and tkyffuotvvxbvn
 Testing for gmbfrnmuca and anrmbufcgm
 Testing for hffddyfiwznsnhsfirz and syfirnisdfnfwdhhfzz
 Testing for ludldirntjyqkwdio and cbmebcqszt
 Testing for xvimwsqcnpihmhwznaj and csjhavpziwmhwnxqimn
 Testing for icsxurgwdqnxbmy and uqgxkheepbp
 Testing for drzmnkdesw and dmdnsrzekw
 Testing for nkteebnrgezztrjsh and rsgriffmtrphwudsgpz
 Testing for twsptdozojz and ztodsoptzjw
 Testing for xcebiekhzwcbaw and lhuaozquwgdtijwaxk
 Testing for wyxtcmynpuicfacxgb and negwwkequry
 Testing for mqczojtojwdgnebsp and snwbtoczjjeogdqpm
 Testing for qdpeuxfbocts and efpbustcdoqx
 Testing for eeycvolpuzziadpjrfsg and ppvsfolerugzaydeczij
 Testing for dpahtgsburr and uiombwizbyfwybmstbrw
 Testing for xdypzoszbajwytkdhimf and dlojjrpayjceuyqwb
 Testing for wjsezrzkncznjd and sjzjendzrkzwnc
 Testing for drnsncmazpbuckettz and mirprppibgzhjib
 Testing for wcmiembtsci and mscewictimb
 Testing for zxtzuqhmstfqfqfhojxy and zxuhqjxtfqtmzsyfhfqo
 Testing for pcdnywfpfywhqmc and nyfqypcwdwpfmch
 Testing for umeazrkxrcjuhz and jeuhrzmxckarzu
 Testing for umcpxslpxuqzbjvdfqiz and hccdapucbokad
 Testing for urhbxsdldpulyvcreuoq and hpsyuedcrlvurqxuldbo
 Testing for gpewrifzmtf and fcolctuagszxry
 Testing for wqjrbfybqckedmbgcber and rjybrbgqmbcewkdqcbfe
 Testing for jhpkshbrrnve and yopcetjpty
 Testing for qdncbobknfm and wdikdfcnhspfuazakl
 Testing for rqxaocfhal and tzvvgpoozjjoh
 Testing for gzcgpexysndexo and sedoxpxngcyzeg
 Testing for rqjexqyaslhfeecvji and otatpuwikm
 Testing for cxmeighndloxqia and hcxadmiegqoxlni
 Testing for ecpolrbjqjqejcuv and jbeopjjqrqveculc
 Testing for buzjgiydthwx and tdwxjybugzhi
 Testing for bqzoovkfgjrvnjqj and jongrqjokjvbvzfq
 Testing for wsgmakecufbuqxawostw and wgqcuametofkuxsbsaww
 Testing for jdufldpkltramxcx and okloqgrwvcat
 Testing for narpvfmhzkfw and fzrpfakhwmvn
 Testing for sofvwrhpebikvebju and gwmhqzloho
 Testing for zepuzrulcypayxgnr and rujzdhfjtumrpcre
 Testing for pckmknucnibm and dcmhvexgqkbiuc
 Testing for cvbmrtbnvkudiyd and yndvdmbbvrikuct
 Testing for uefpgjliwbc and biflcjepgwu
 Testing for stelewodrgmeemipmvvr and msgvrpetwlmmreeeviod
 Testing for mpqfxavcmwqfu and cupqffxmmwqav
 Testing for gumtpxhibrfnybko and fxlgpketdnoim
 Testing for lptbzsiavjkdsmuk and yswdvaiethfvavdtmyeo
 Testing for tzrpzpfalbrv and apzflvrztprb
 Testing for ieibpsnzksupx and ssiipkebnxpuz
 Testing for pkywmmfsrgql and pvrortbqyh
 Testing for hpijsxtbkgbrhyuawba and strakbbajghwiuybphx
 Testing for irjmystmfpsg and nbbyumncsytlsteb
 Testing for uylwexooia and ixuowyaelo
 Testing for zprfcumrgvlnxp and mvnxpulgrzfpcr
 Testing for anpaydnetndbr and pcfivpwyiuwp
 Testing for fotnohlrmkocca and hbkkfnqkucasjetkaqz
 Testing for iaqfmplhznqsha and amphqlfqzashin
 Testing for npnspvlszbalxxifks and pfaszkipssvnxxlnbl
 Testing for rmbwsjdhujaxna and ykgjtozoxre
 Testing for hlqfuptfwsugrs and ojftnefiqoltxqccawn
 Testing for okanqwcstgnhkartkndn and jwpruxxugesd
 
  STDERR
Execution Timed Out (12000 ms)

Why did my code time out?
Our servers are configured to only allow a certain amount of time for your code to execute. In rare cases the server may be taking on too much work and simply wasn't able to run your code efficiently enough. Most of the time though this issue is caused by inefficient algorithms. If you see this error multiple times you should try to optimize your code further.

some tests had up to 600,000 characters?
 Performance tests
 Testing for two strings up to 600000 characters
'''