import fresh_tomatoes
import media


forrest_gump = media.Movie(
    "Forrest Gump",
    "http://www.impawards.com/1994/posters/forrest_gump.jpg",
    "Robert Zemeckis",
    "Tom Hanks, Sally Field, Robin Wright",
    "1994",
    "https://youtu.be/bLvqoHBptjg")

the_matrix = media.Movie(
    "The Matrix",
    "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
    "Lana Wachowski",
    "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
    "1999",
    "https://youtu.be/vKQi3bBA1y8")

titanic = media.Movie(
    "Titanic", 
    "http://www.impawards.com/1997/posters/titanic_ver2.jpg", 
    "James Cameron", 
    "Kate Winslet, Leonardo DiCaprio, Frances Fisher",
    "1997",
    "https://youtu.be/2e-eXJ6HgkQ")

avatar = media.Movie(
    "Avatar", 
    "http://www.impawards.com/2009/posters/avatar.jpg",
    "James Cameron",
    "Sam Worthington, Zoe Saldana, Sigourney Weaver",
    "2009",
    "https://youtu.be/5PSNL1qE6VY")

inception = media.Movie(
    "Inception",
    "http://www.impawards.com/2010/posters/inception_ver2.jpg",
    "Christopher Nolan",
    "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
    "2010",
    "https://youtu.be/8hP9D6kZseM")

social_network = media.Movie(
    "Social Network",
    "http://www.impawards.com/2010/posters/social_network.jpg",
    "David Fincher",
    "Jesse Eisenberg, Andrew Garfield, Justin Timberlake",
    "2010",
    "https://youtu.be/lB95KLmpLR4")

finding_dory = media.Movie(
    "Finding Dory",
    "http://www.impawards.com/2016/posters/finding_dory.jpg",
    "Andrew Stanton",
    "Ellen DeGeneres, Albert Brooks, Diane Keaton",
    "2016",
    "https://youtu.be/MKJA-VLpiCo")

tarzan = media.Movie(
    "Tarzan",
    "http://www.impawards.com/2016/posters/tarzan.jpg",
    "David Yates",
    "Alexander Skarsgard, Margot Robbie, Christoph Waltz",
    "2016",
    "https://youtu.be/dLmKio67pVQ")

edward_scissorhands = media.Movie(
    "Edward Scissorhands",
    "http://www.impawards.com/1990/posters/edward_scissorhands_ver1.jpg",
    "Tim Burton",
    "Johnny Depp, Winona Ryder, Dianne Wiest",
    "1990",
    "https://youtu.be/M94yyfWy-KI")

mulan = media.Movie(
    "Mulan",
    "http://www.impawards.com/1998/posters/mulan_ver1.jpg",
    "Barry Cook",
    "Ming-Na Wen, Lea Salonga, June Foray",
    "1998",
    "https://youtu.be/wAbGAkkOgcM")

the_godfather = media.Movie(
    "The Godfather",
    "http://www.impawards.com/1972/posters/godfather_ver1.jpg",
    "Francis Ford Coppola",
    "Marlon Brando, Al Pacino, James Caan",
    "1972",
    "https://youtu.be/sY1S34973zA")

fight_club = media.Movie(
    "Fight Club",
    "http://www.impawards.com/1999/posters/fight_club_ver2.jpg",
    "David Fincher",
    "Edward Norton, Brad Pitt, Helena Bonham Carter",
    "1999",
    "https://youtu.be/SUXWAEX2jlg")


movies = [
    forrest_gump, the_matrix,
    titanic, avatar, inception,
    social_network, finding_dory, 
    tarzan, edward_scissorhands, 
    mulan, the_godfather, fight_club]

fresh_tomatoes.open_movies_page(movies)
