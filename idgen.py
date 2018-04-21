import zlib
import random
import datetime
maxpop = 280728988
woman_names = [
    'Maria','Jane','Stacy','Merideth','Beth','Angela','Mary','Tiffany',
    'Pamela','April','Louise','Virginia','Nicole','Carolyn','Julia','Trina',
    'Robin','Karen','Susan','Kathy','Shirley','Renee','Olivia','Beth','Gladys',
    'Dianne','Ethelene','Patricia','Anne','Kathleen','Carol','Kimberly',
    'Marcia','Marsha','Sharon','Ella','Evelyn','Glenda','Katie','Kate','Ann',
    'Dana','Shannon','Elizabeth','Lillian','Jo Ann','Karen','Edith','Jenny',
    'Deborah','Elisa','Becky','Barbara','Blair','Cynthia','Debbie','Diane',
    'Margaret','Racheal','Shari','Gail','Sarah','Cathy','Katrina','Marlene',
    'Patricia','Lisa','Candace','Beatrice','Betty','Wendy','Denise','Rebecca',
    'Arlene','Stephanie','Flora','Martha','Nancy','Tanya','Helen','Patty',
    'Della','Ida','Lisa','Jeanne','Theresa','Vanessa','Rose','Benita','Lucy',
    'Suzette','Jessica','Blair','Gina','Melissa','Nikki','Victoria',
    'Priscilla','Catherine','Joan','Sue','Sonja','Stephanie','Cindy','Alison',
    'Samantha','Kelly','Carroll','Lauren','Louis','Alicia','Sylvia','Jenn',
    'Theodora','Leanne','Krissy','Belle','Mandy','Erin','Marylin']
man_names = [
    'Michael','Mike','Randy','Richard','Ronald','Samuel','Scott','Willie',
    'Stanley','William','Burt','Bob','Steve','Jason','Dennis','Joe','Jim',
    'John','Robert','Sidney','Walter','Keith','David','Gwen','Thomas','Bill',
    'Don','James','Alfred','Andrew','Arnold','Bruce','Bryan','Clyde','Charles',
    'Doug','Dwight','Dwayne','Edward','Eric','Chris','Mark','Harry','Jerry',
    'Leroy','George','Samuel','Wesley','Terry','Jeff','Franklin','Melvin',
    'Marcus','Rudy','Jimmy','Eddie','Lewis','Ralph','Kenneth','Phillip',
    'Gregory','Howard','Geoff','Theo','Jeffrey','Paul','Cliff','Darrell',
    'Christopher','Anthony','Chuck','Sam','Phil','Fredrick','Johnny','Hugh',
    'Alvin','Alan','Buck','Bo','Dewitt','Tom','Tony','Lawrence','Roger','Marc',
    'Cecil','Kevin','Maurice','Byron','Patrick','Johnie','Daniel','Edwin',
    'Jesse','Leonard','Andy','Norman','Eugene','Jerrell']
surnames = [
    'Abbot','Abe','Abrams','Acker','Ackman','Adams','Adam','Adamson','Addison',
    'Adkins','Adler','Allen','Alford','Allison','Alley','Allgood','Anderson',
    'Amos','Applegate','Apple','Arnold','Ashby','Austin','Austin','Baker',
    'Baldwin','Banks','Bannerman','Barber','Barfield','Barkley','Barnett',
    'Barry','Basinger','Bays','Beck','Bell','Benjamin','Bennett','Bentley',
    'Biggs','Binder','Blackburn','Blackwood','Blake','Bobbitt','Boggs',
    'Bolden','Borden','Bosworth','Bowden','Bowen','Bowers','Bowman','Bradley',
    'Brady','Briggs','Britt','Brown','Bullock','Burton','Byrd','Carlon',
    'Carter','Casey','Cates','Caudle','Chambers','Chandler','Chapman','Chavis',
    'Cheek','Clapp','Clark','Clarke','Clemmons','Cline','Cobb','Coble','Cole',
    'Coleman','Collins','Combs','Compton','Conner','Connor','Conway','Cook',
    'Cowan','Cox','Crawford','Crutchfield','Cunningham','Daniel','Darnell',
    'Davis','Day','Dawson','Dixon','Douglas','Dunn','Edwards','Ellis',
    'Ellison','Emmett','Erwin','Evans','Evenson','Everhart','Farlow','Fann',
    'Ferguson','Fields','Fish','Fitzgerald','Flowers','Forrest','Foster',
    'Fowler','Frazier','Free','Freeman','Frye','Fulk','Fulton','Furr',
    'Galloway','Gardner','Gaulden','Gauley','Gerkin','Getters','Gibbs',
    'Gibson','Gilbert','Gillett','Glass','Glenn','Glover','Goble','Godfrey',
    'Goldston','Goldstein','Good','Gordon','Gorham','Gorrell','Gossett',
    'Graham','Grant','Graves','Gray','Green','Garfield','Greene','Gregory',
    'Gross','Gwynn','Hager','Haines','Hairston','Ham','Hamilton','Hammond',
    'Hanks','Hampton','Hamrick','Harden','Hardy','Hare','Harper','Harrel',
    'Harris','Harrison','Hart','Hatfield','Hayes','Haynes','Helms','Henderson',
    'Hendricks','Henley','Henson','Hester','Hatt','Hickman','Hicks','Higgins',
    'Hill','Hines','Hinshaw','Hinson','Hodges','Hobson','Holder','Holl',
    'Holiday','Holloway','Holt','Hoover','Hopkins','Horn','Hoskins','Hubbard',
    'Hudson','Huff','Huffman','Hughes','Huneycutt','Hurst','Hutchers','Hylton',
    'Irel','Irwin','Isley','Jaby','Jackson','Jacob','Jarrell','Jester',
    'Johnson','Jones','Jordan','Joseph','Joyner','Justice','Keith','Kelley',
    'Kellis','Kendall','Kennedy','Kenny','Kim','Kimble','King','Kinsey',
    'Kirkman','Kiser','Knight','Knott','Lamb','Lambert','Lambeth','Lacey',
    'Lane','Lang','Langley','Lankford','Lashley','Lawson','Leary','Leggett',
    'Legrant','Lemonds','Lanahan','Leonard','Lewis','Lineback','Lindsay',
    'Little','Lloyd','Livengood','Locke','Long','Lord','Love','Lovett','Lucas',
    'Lowe','Lyons','Mabe','Mackey','Maddox','Maness','Mangum','Mann','Manning',
    'Marion','Marks','Marsh','Marshall','Martin','Martinez','Mathews','Mathis',
    'Matthews','May','Mayer','McClain','McConnell','McCormick','McCraw',
    'McCullough','McDougald','McPherson','Medlin','Melvin','Mentis','Meyer',
    'Middleton','Miller','Mitchell','Montgomery','Moore','Morrison','Morrow',
    'Morton','Moss','Murphy','Murray','Neal','Newnam','Newton','Nichols',
    'Nixon','Norris','Norton','Nunn','O''Brien','O''Donnel','Oldham','Olds',
    'Oliver','Olson','O''Neal','Osborne','Owens','Padgett','Pace','Page',
    'Painter','Parker','Parrish','Parsons','Patel','Patterson','Peacock',
    'Pennington','Perkins','Peterson','Phillips','Pickard','Pickett','Piper',
    'Pitts','Pleasants','Poole','Pope','Posey','Potter','Powers','Prendergast',
    'Pressley','Preston','Priddy','Pugh','Purcell','Purvis','Putnam','Quick',
    'Raines','Ramsey','Rankin','Reese','Reeves','Reid','Richards','Rich',
    'Riches','Richter','Riley','Ring','Ripley','Rippy','Rivera','Roberts',
    'Robertson','Robinson','Rodgers','Rogers','Roseboro','Rosen','Ross',
    'Rouse','Royal','Rucker','Russell','Saunders','Sawyer','Scott','Seawell',
    'Shannon','Sharples','Shaw','Shelton','Shoffner','Short','Showfety',
    'Simmons','Sims','Singer','Small','Smith','Snyder','Southern','Spencer',
    'Staley','Stanley','Stephens','Stephenson','Stevens','Stewart','Stone',
    'Stricklen','Swann','Sumner','Swaney','Talbert','Tate','Taylor','Thomas',
    'Thompson','Thorne','Townsend','Troxler','Turner','Tuttle','Tyson',
    'Umfleet','Underwood','Utley','Vance','Vanstory','Vines','Vaughan',
    'Vestall','Walker','Wall','Wallace','Walters','Ward','Warren','Washington',
    'Watkins','Watson','Wayne','Weaver','Webb','Webster','Wells','West',
    'White','Wilkins','Williams','Wilson','Young','Zimmerman']
streets = [
    'River St.','Lindley Ave.','Ray St.','Chruch St.','Carriage Ln.',
    'Ludwick Ln.','Quate Dr.','Summit Av.','Greenbrair Rd.','Olive St.',
    'Pinelake Dr.','Orchard St.','Smokeridge Ln.','Coleridge Dr.',
    'Branson Rd.','Cardigan St.','Main St.','Cottage Av.',
    'Mr. Luther King Dr.','Westworth Dr.','Hillsdale St.','New Garden Rd.',
    'Oak Ridge Rd.','Cascade Ln.','Lakebend Way','Deerwood Dr.',
    'Northwood Ave.','Woodstream Rd.','Leawood Dr.','Grayston Ln.','Knox Rd.',
    'Bears Creek Rd.','Simons Sq.','Washington St.','Market St.','Country Dr.',
    'Grove Ln.','Hilltop Rd.','Sherwood St.','Folger Rd.','Company Mill Ln.',
    'Nelson St.','Hedrick Dr.','Cottage Pl.','United St.','Hewitt St.',
    'Walker Ave.','Burns St.','Raintree Ln.','Juliet Dr.','Garlston Dr.',
    'Kingston St.','Elm St.','Quaker Ave.','Rollingwood Dr.','Tower Rd.',
    'Lakepoint Dr.','Chapman St.','Boyd Rd.','Ross Av.','Dogwood Dr.',
    'Fisher Park Pl.','Murphy Rd.','Summertree Ave.','Bluemont Dr.',
    'Weslo St.','Flint St.','Stillwell Rd.','Bingham St.','Kenview Ave.']
d = zlib.decompress(open('zipdb.bin','rb').read()).split(b'\x0a')
sr = random.SystemRandom()
ppl_id = sr.randrange(maxpop)
ppl_sum = 0
for line in d:
    p=line.find(b';')+1
    ppl_sum += int(line[p:line.find(b';',p)])
    if ppl_sum>ppl_id:
        s = line.decode('cp1252')
        break
s = s.split(';')
ZipCode = s[0]
MalePopulation = int(s[2])
FemalePopulation = int(s[3])
isMale = sr.randrange(MalePopulation + FemalePopulation) < MalePopulation
if isMale:
    Age = float(s[4])
else:
    Age = float(s[5])
Latitude = float(s[6])
Longitude = float(s[7])
Elevation = int(s[8])
State = s[9]
StateFullName = s[10]
CityAliasAbbreviation = s[11]
AreaCode = sr.choice(s[12].split('/'))
City = s[13].title()
CountyName = s[14].title()
CountyFIPS = s[15]
StateFIPS = s[16]
TimeZone = s[17]
DayLightSaving = s[18]
CBSA_Name = s[19]
Region = s[20]
Division = s[21]
PreferredLastLineKey = s[22]
CBSA_Div_Name = s[23]
FirstName = sr.choice(man_names) if isMale else sr.choice(woman_names)
LastName = sr.choice(surnames)
Street = sr.choice(streets)
Phone = AreaCode + '-' + str(sr.randrange(200, 970+1)) + '-' + str(sr.randrange(1000, 9990+1))
Address = str(sr.randrange(50, 3000+1)) + ' ' + Street
print(FirstName + ' ' + LastName)
print(Address)
print(City + ', ' + State + ' ' + ZipCode + '\n')
print('--- Additional info ---')
print('First Name:           ' + FirstName)
print('Last Name:            ' + LastName)
print('Sex:                  ' + ('Male' if isMale else 'Female'))
print('Age:                  ' + str(Age))
print('Estimated D.O.B.:     ' + str(datetime.date.fromordinal(round(datetime.date.today().toordinal()-365.25*Age))))
print('Address:              ' + Address)
print('City:                 ' + City)
print('State:                ' + State + ' (' + StateFullName + ')')
print('Zip code:             ' + ZipCode)
print('Phone number:         ' + Phone)
print('Latitude:             ' + str(Latitude))
print('Longitude:            ' + str(Longitude))
print('Elevation:            ' + str(Elevation) + ' m')
print('Time zone:            ' + TimeZone)
print('Daylight saving:      ' + DayLightSaving)
if CityAliasAbbreviation:
    print('City abbr.:           ' + CityAliasAbbreviation)
print('County name:          ' + CountyName)
print('County FIPS:          ' + CountyFIPS)
print('State FIPS:           ' + StateFIPS)
if Region:
    print('Region:               ' + Region)
if Division:
    print('Division:             ' + Division)
if CBSA_Name:
    print('CBSA name:            ' + CBSA_Name)
if CBSA_Div_Name:
    print('CBSA division name:   ' + CBSA_Div_Name)
print('PreferredLastLineKey: ' + PreferredLastLineKey)
