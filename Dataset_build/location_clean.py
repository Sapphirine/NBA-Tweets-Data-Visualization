import json
import googlemaps
gmaps = googlemaps.Client(key='0')

with open('teams1.json') as ifile:    
    datas = json.load(ifile)
ofile = open('clean1.json', 'a')
print('done')

num = 0
for data in datas:
    if num < 32673:
        num += 1
        continue
    idict = {}
    idict['name'] = data.get('user').get('name')
    idict['time'] = data.get('created_at')
    idict['text'] = data.get('text')
    idict['id'] = data.get('id')
    place = data.get('user').get('location')
    str = data.get('text').lower()
    idict['team'] = None
    if str.find("dennis schröder") != -1 or str.find("marco belinelli") != -1 or str.find("ersan ilyasova") != -1 or str.find("mike muscala") != -1 or str.find("kent bazemore") != -1 or str.find("atlanta hawks") != -1:
        idict['team'] = "hawks"
    elif str.find("kemba walker") != -1 or str.find("nicolas batum") != -1 or str.find("michael kidd-gilchrist") != -1 or str.find("marvin williams") != -1 or str.find("	dwight howard") != -1 or str.find("charlotte hornets") != -1: 
        idict['team'] = "hornets"
    elif str.find("goran dragic") != -1 or str.find("dion waiters") != -1 or str.find("josh richardson") != -1 or str.find("james johnson") != -1 or str.find("kelly olynyk") != -1 or str.find("miami heat") != -1:
        idict['team'] = "heat"
    elif str.find("elfrid payton") != -1 or str.find("evan fournier") != -1 or str.find("jonathon simmons") != -1 or str.find("aaron gordon") != -1 or str.find("nikola vucevic") != -1 or str.find("orlando magic") != -1:
        idict['team'] = "magic"
    elif str.find("tim frazier") != -1 or str.find("bradley beal") != -1 or str.find("kelly oubre jr.") != -1 or str.find("otto porter") != -1 or str.find("marcin gortat") != -1 or str.find("washington wizards") != -1:
        idict['team']= "wizards"
    elif str.find("kris dunn") != -1 or str.find("justin holiday") != -1 or str.find("denzel valentine") != -1 or str.find("lauri markkanen") != -1 or str.find("robin lopez") != -1 or str.find("chicago bulls") != -1:
        idict['team'] = "bulls"
    elif str.find("jose calderon") != -1 or str.find("j.r. smith") != -1 or str.find("lebron james") != -1 or str.find("jae crowder") != -1 or str.find("kevin love") != -1 or str.find("cleveland cavaliers") != -1:
        idict['team'] = "cavaliers"
    elif str.find("reggie jackson") != -1 or str.find("avery bradley") != -1 or str.find("stanley johnson") != -1 or str.find("tobias harris") != -1 or str.find("andre drummond") != -1 or str.find("detroit pistons") != -1:
        idict['team'] = "pistons"
    elif str.find("kyrie irving") != -1 or str.find("jaylen brown") != -1 or str.find("jayson tatum") != -1 or str.find("marcus morris") != -1 or str.find("al horford") != -1 or str.find("boston celtics") != -1:
        idict['team'] = "celtics"
    elif str.find("spencer dinwiddie") != -1 or str.find("allen crabbe") != -1 or str.find("demarre carroll") != -1 or str.find("rondae hollis-jefferson") != -1 or str.find("timofey mozgov") != -1 or str.find("brooklyn nets") != -1:
        idict['team'] = "nets"
    elif str.find("jarrett jack") != -1 or str.find("damyean dotson") != -1 or str.find("courtney lee") != -1 or str.find("kristaps porzingis") != -1 or str.find("enes kanter") != -1 or str.find("new york knicks") != -1:
        idict['team'] = "knicks"
    elif str.find("dennis smith") != -1 or str.find("yogi ferrell") != -1 or str.find("wesley matthews") != -1 or str.find("harrison barnes") != -1 or str.find("dirk nowitzki") != -1 or str.find("dallas mavericks") != -1:
        idict['team'] = "mavericks"
    elif str.find("chris paul") != -1 or str.find("james harden") != -1 or str.find("trevor ariza") != -1 or str.find("ryan anderson") != -1 or str.find("clint capela") != -1 or str.find("houston rockets") != -1:
        idict['team'] = "rockets"
    elif str.find("mario chalmers") != -1 or str.find("james ennis iii") != -1 or str.find("dillon brooks") != -1 or str.find("jarell martin") != -1 or str.find("marc gasol") != -1 or str.find("memphis grizzlies") != -1:
        idict['team'] = "grizzlies"
    elif str.find("steph curry") != -1 or str.find("klay thompson") != -1 or str.find("kevin durant") != -1 or str.find("draymond green") != -1 or str.find("zaza pachulia") != -1 or str.find("golden state warriors") != -1:
        idict['team'] = "warriors"
    elif str.find("austin rivers") != -1 or str.find("lou williams") != -1 or str.find("wesley johnson") != -1 or str.find("danilo gallinari") != -1 or str.find("deandre jordan") != -1 or str.find("los angeles clippers") != -1:
        idict['team'] = "clippers"
    elif str.find("lonzo ball") != -1 or str.find("kentavious caldwell-pope") != -1 or str.find("brandon ingram") != -1 or str.find("larry nance jr.") != -1 or str.find("brook lopez") != -1 or str.find("los angeles lakers") != -1:
        idict['team'] = "lakers"
    elif str.find("jamal murray") != -1 or str.find("gary harris") != -1 or str.find("wilson chandler") != -1 or str.find("kenneth faried") != -1 or str.find("nikola jokic") != -1 or str.find("denver nuggets") != -1: 
        idict['team'] = "nuggets"
    elif str.find("jeff teague") != -1 or str.find("jimmy butler") != -1 or str.find("andrew wiggins") != -1 or str.find("taj gibson") != -1 or str.find("karl-anthony towns") != -1 or str.find("minnesota timberwolves") != -1:
        idict['team'] = "timberwolves"
    elif str.find("russell westbrook") != -1 or str.find("andre roberson") != -1 or str.find("paul george") != -1 or str.find("carmelo anthony") != -1 or str.find("steven adams") != -1 or str.find("oklahoma city thunder") != -1:
        idict['team'] = "thunder"
    elif str.find("darren collison") != -1 or str.find("victor oladipo") != -1 or str.find("bojan bogdanovic") != -1 or str.find("thaddeus young") != -1 or str.find("myles turner") != -1 or str.find("indiana pacers") != -1:
        idict['team'] = "pacers"
    elif str.find("eric bledsoe") != -1 or str.find("tony snell") != -1 or str.find("khris middleton") != -1 or str.find("giannis antetokounmpo") != -1 or str.find("john henson") != -1 or str.find("milwaukee bucks") != -1:
        idict['team'] = "bucks"
    elif str.find("jerryd bayless") != -1 or str.find("j.j. redick") != -1 or str.find("ben simmons") != -1 or str.find("robert covington") != -1 or str.find("joel embiid") != -1 or str.find("philadelphia 76ers") != -1:
        idict['team'] = "sixers"
    elif str.find("kyle lowry") != -1 or str.find("demar derozan") != -1 or str.find("c.j. miles") != -1 or str.find("serge ibaka") != -1 or str.find("jonas valanciunas") != -1 or str.find("toronto raptors") != -1:
        idict['team'] = "raptors"
    elif str.find("rajon rondo") != -1 or str.find("jrue holiday") != -1 or str.find("e'twaun moore") != -1 or str.find("anthony davis") != -1 or str.find("demarcus cousins") != -1 or str.find("new orleans pelicans") != -1:
        idict['team'] = "pelicans"
    elif str.find("tony parker") != -1 or str.find("danny green") != -1 or str.find("kyle anderson") != -1 or str.find("lamarcus aldridge") != -1 or str.find("pau gasol") != -1 or str.find("san antonio spurs") != -1:
        idict['team'] = "spurs"
    elif str.find("tyler ulis") != -1 or str.find("troy daniels") != -1 or str.find("t.j. warren") != -1 or str.find("marquese chriss") != -1 or str.find("tyson chandler") != -1 or str.find("phoenix suns") != -1:
        idict['team'] = "suns"
    elif str.find("george hill") != -1 or str.find("garrett temple") != -1 or str.find("bogdan bogdanovic") != -1 or str.find("zach randolph") != -1 or str.find("willie cauley-stein") != -1 or str.find("sacramento kings") != -1:
        idict['team'] = "kings"
    elif str.find("damian lillard") != -1 or str.find("c.j. mccollum") != -1 or str.find("al-farouq aminu") != -1 or str.find("noah vonleh") != -1 or str.find("jusuf nurkic") != -1 or str.find("portland trail blazers") != -1:
        idict['team'] = "blazers"
    elif str.find("ricky rubio") != -1 or str.find("donovan mitchell") != -1 or str.find("joe ingles") != -1 or str.find("derrick favors") != -1 or str.find("rudy gobert") != -1 or str.find("utah jazz") != -1:
        idict['team'] = "jazz"
    if idict['team'] is not None:
        geocode_result = gmaps.geocode(place)
        if geocode_result != []:
            if geocode_result[0] != []:
                address = geocode_result[0]['address_components']
                for lines in address:
                    if lines != [] and lines['types'] != [] and lines['types'][0] == "administrative_area_level_1":
                        idict['state'] = lines['long_name']
                        num += 1
                        json.dump(idict, ofile)
                        ofile.write(',')
                        ofile.write('\n')
                        print(num)
                        print(idict['state'])
ofile.close()