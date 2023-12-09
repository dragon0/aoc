@main def hello: Unit =
  println("Hello world!")
  println(msg)

def msg = "I was compiled by Scala 3. :)"

val gamePattern = """Game (\d+)""".r

case class Game(id: Int, revelations: List[Map[String, Int]])

def part1(input: String): Int =
  var total = 0
  for inputLine <- input.split('\n')
  do
    val game = parseGame(inputLine)
    if gameIsValid(game) then total += game.id
  total

def part2(input: String): Int =
  input.split('\n').map(parseGame(_)).map(findMaxes(_).product).sum

def parseGame(inputLine: String): Game =
  inputLine.split(':') match
    case Array(gameString, revelationsString) =>
      gameString match
        case gamePattern(gameIdString) =>
          val gameId = gameIdString.toInt
          var revelations: List[Map[String, Int]] = Nil
          for revelationString <- revelationsString.split(';')
          do
            var revelation: Map[String, Int] = Map()
            for revelationPart <- revelationString.split(',')
            do
              revelationPart.trim().split(' ') match
                case Array(countString, color) =>
                  revelation = revelation + (color -> countString.toInt)

            revelations = revelation :: revelations
          Game(gameId, revelations)

def gameIsValid(game: Game): Boolean =
  game.revelations forall { r =>
    r.getOrElse("red", 0) <= 12 &&
    r.getOrElse("green", 0) <= 13 &&
    r.getOrElse("blue", 0) <= 14
  }

def findMaxes(game: Game): List[Int] =
  game.revelations.flatten
    .groupBy(_._1)
    .mapValues(_.map(_._2).reduce(Integer.max(_, _)))
    .values
    .toList
