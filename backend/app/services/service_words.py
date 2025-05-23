import random
import numpy as np

english_words = [
    "apple", "banana", "carrot", "dog", "elephant", "flower", "giraffe", "house", "island", "jungle",
    "kangaroo", "lion", "mountain", "notebook", "orange", "pencil", "queen", "rabbit", "sun", "tree",
    "umbrella", "violin", "water", "xylophone", "yellow", "zebra", "airport", "basket", "candle", "diamond",
    "engine", "forest", "garden", "hammer", "igloo", "jacket", "kitchen", "ladder", "mirror", "necklace",
    "ocean", "piano", "quilt", "rocket", "sandwich", "tiger", "uniform", "village", "window", "yacht",
    "airplane", "butterfly", "camera", "dolphin", "eagle", "fireplace", "guitar", "hamburger", "iceberg", "jellyfish",
    "koala", "lighthouse", "mushroom", "napkin", "octopus", "penguin", "quokka", "rhinoceros", "strawberry", "turtle",
    "unicorn", "volcano", "watermelon", "xylophone", "yogurt", "zeppelin", "anchor", "bubble", "coconut", "dragon",
    "feather", "globe", "honey", "island", "jigsaw", "kettle", "lantern", "mango", "nest", "olive",
    "peach", "quail", "raccoon", "sailboat", "tulip", "urchin", "violet", "whale", "xenon", "yarrow",
    "acorn", "blossom", "cactus", "daisy", "echo", "flamingo", "gazebo", "horizon", "ivy", "jade",
    "kiwi", "lily", "maple", "nutmeg", "orchid", "peony", "quartz", "rose", "sunflower", "thistle",
    "upbeat", "vanilla", "willow", "xeric", "yucca", "zinnia", "amber", "brook", "cliff", "dew",
    "earth", "fog", "glacier", "hail", "ice", "jetty", "kayak", "lagoon", "mist", "nimbus",
    "oasis", "pond", "quarry", "rain", "stream", "tide", "undulate", "vapor", "wave", "yonder",
    "alabaster", "breeze", "cascade", "drizzle", "ember", "frost", "gale", "haze", "inferno", "jovial",
    "kaleidoscope", "luminous", "meadow", "nectar", "opal", "prism", "quasar", "radiant", "serene", "twilight",
    "umbra", "vivid", "whirl", "xenial", "yearn", "zephyr", "azure", "bliss", "cosmic", "dream",
    "ethereal", "fable", "glow", "harmony", "inspire", "jubilant", "kismet", "lullaby", "melody", "nirvana",
    "oceanic", "paradise", "quaint", "reverie", "solace", "tranquil", "utopia", "velvet", "wonder", "xanadu",
    "yoga", "zen", "adventure", "brave", "courage", "discover", "explore", "freedom", "gallant", "heroic",
    "imagine", "journey", "knight", "legend", "mystery", "noble", "odyssey", "pioneer", "quest", "rebel",
    "spirit", "trailblazer", "unconquerable", "valiant", "wander", "xenophile", "yonder", "zeal", "artistic", "brilliant",
    "creative", "daring", "expressive", "fascinating", "genius", "harmonious", "inventive", "joyful", "keen", "lively",
    "masterful", "notable", "original", "passionate", "quirky", "remarkable", "sensitive", "talented", "unique", "visionary",
    "whimsical", "exuberant", "youthful", "zesty", "active", "bold", "cheerful", "dynamic", "energetic", "fearless",
    "gutsy", "hardy", "intrepid", "jovial", "kind", "loyal", "mighty", "nice", "optimistic", "powerful",
    "quick", "resilient", "strong", "tenacious", "unstoppable", "vigorous", "witty", "excellent", "yielding", "zany",
    "abstract", "bizarre", "curious", "different", "eccentric", "funky", "groovy", "hip", "irregular", "jagged",
    "kooky", "lopsided", "messy", "nonsense", "odd", "peculiar", "quizzical", "random", "strange", "twisted",
    "unusual", "vague", "weird", "xenomorphic", "yawning", "zigzag", "amazing", "beautiful", "colorful", "delightful",
    "elegant", "fabulous", "gorgeous", "handsome", "incredible", "jolly", "kaleidoscopic", "lovely", "magnificent", "nice",
    "outstanding", "pretty", "quality", "radiant", "splendid", "terrific", "unique", "vibrant", "wonderful", "xenial",
    "yummy", "zesty", "agile", "balanced", "coordinated", "deft", "elastic", "flexible", "graceful", "healthy",
    "intact", "jumpy", "kinetic", "limber", "mobile", "nimble", "orderly", "poised", "quick", "robust",
    "supple", "tough", "upright", "vigorous", "well", "xeric", "yielding", "zippy", "accurate", "bright",
    "clear", "detailed", "exact", "factual", "genuine", "honest", "intelligent", "just", "knowledgeable", "logical",
    "meticulous", "notable", "objective", "precise", "quality", "real", "sound", "true", "unbiased", "valid",
    "wise", "xenial", "yare", "zealous", "ample", "big", "colossal", "enormous", "gigantic", "huge",
    "immense", "jumbo", "king-size", "large", "massive", "monumental", "oversized", "prodigious", "queen-size", "roomy",
    "spacious", "titanic", "untold", "vast", "wide", "x-large", "yawning", "whopping", "aromatic", "biting",
    "citrusy", "delicious", "earthy", "flavorful", "garlicky", "herbal", "juicy", "kicky", "lemony", "minty",
    "nutty", "oniony", "peppery", "quality", "rich", "savory", "tangy", "umami", "vinegary", "woodsy",
    "yummy", "zesty", "adorable", "beautiful", "cute", "dazzling", "elegant", "fancy", "glamorous", "handsome",
    "irresistible", "jolly", "kittenish", "lovely", "magnificent", "neat", "opulent", "pretty", "quaint", "radiant",
    "sparkling", "trim", "upbeat", "vibrant", "winsome", "xenial", "youthful", "zany", "acoustic", "blaring",
    "chiming", "deafening", "euphonic", "faint", "harmonic", "insistent", "jazzy", "lyrical", "melodic", "noisy",
    "operatic", "piercing", "quiet", "raucous", "sonorous", "thundering", "ululating", "vocal", "whispering", "xylophonic",
    "yodeling", "zingy", "ancient", "bygone", "colonial", "dated", "early", "former", "historical", "old",
    "past", "prehistoric", "primitive", "remote", "retro", "stone-age", "traditional", "vintage", "antique", "yesteryear",
    "zippy", "ample", "bountiful", "copious", "dense", "enough", "filled", "generous", "heavy", "infinite",
    "jam-packed", "lavish", "loaded", "many", "numerous", "overflowing", "packed", "quite", "replete", "sufficient",
    "teeming", "untold", "vast", "whole", "extensive", "yawning", "zillion", "adorable", "blissful", "content",
    "delighted", "ecstatic", "festive", "glad", "happy", "jolly", "joyful", "kind", "laughing", "merry",
    "nice", "optimistic", "pleasant", "quality", "rosy", "smiling", "thrilled", "upbeat", "vivacious", "wonderful",
    "xenial", "yummy", "zany", "authentic", "best", "correct", "genuine", "honest", "legitimate", "original",
    "pure", "real", "right", "true", "valid", "actual", "certain", "factual", "for-real", "kosher",
    "natural", "positive", "precise", "proper", "rightful", "sincere", "sound", "sterling", "sure-enough", "true-blue",
    "unfeigned", "veritable", "well-grounded", "xenial", "yare", "zealous", "ample", "big", "colossal", "enormous",
    "gigantic", "huge", "immense", "jumbo", "king-size", "large", "massive", "monumental", "oversized", "prodigious",
    "queen-size", "roomy", "spacious", "titanic", "untold", "vast", "wide", "x-large", "yawning", "whopping",
    "aromatic", "biting", "citrusy", "delicious", "earthy", "flavorful", "garlicky", "herbal", "juicy", "kicky",
    "lemony", "minty", "nutty", "oniony", "peppery", "quality", "rich", "savory", "tangy", "umami",
    "vinegary", "woodsy", "yummy", "zesty", "adorable", "beautiful", "cute", "dazzling", "elegant", "fancy",
    "glamorous", "handsome", "irresistible", "jolly", "kittenish", "lovely", "magnificent", "neat", "opulent", "pretty",
    "quaint", "radiant", "sparkling", "trim", "upbeat", "vibrant", "winsome", "xenial", "youthful", "zany",
    "acoustic", "blaring", "chiming", "deafening", "euphonic", "faint", "harmonic", "insistent", "jazzy", "lyrical",
    "melodic", "noisy", "operatic", "piercing", "quiet", "raucous", "sonorous", "thundering", "ululating", "vocal",
    "whispering", "xylophonic", "yodeling", "zingy", "ancient", "bygone", "colonial", "dated", "early", "former",
    "historical", "old", "past", "prehistoric", "primitive", "remote", "retro", "stone-age", "traditional", "vintage",
    "antique", "yesteryear", "zippy", "ample", "bountiful", "copious", "dense", "enough", "filled", "generous",
    "heavy", "infinite", "jam-packed", "lavish", "loaded", "many", "numerous", "overflowing", "packed", "quite",
    "replete", "sufficient", "teeming", "untold", "vast", "whole", "extensive", "yawning", "zillion", "adorable",
    "blissful", "content", "delighted", "ecstatic", "festive", "glad", "happy", "jolly", "joyful", "kind",
    "laughing", "merry", "nice", "optimistic", "pleasant", "quality", "rosy", "smiling", "thrilled", "upbeat",
    "vivacious", "wonderful", "xenial", "yummy", "zany", "authentic", "best", "correct", "genuine", "honest",
    "legitimate", "original", "pure", "real", "right", "true", "valid", "actual", "certain", "factual",
    "for-real", "kosher", "natural", "positive", "precise", "proper", "rightful", "sincere", "sound", "sterling",
    "sure-enough", "true-blue", "unfeigned", "veritable", "well-grounded", "xenial", "yare", "zealous", "ample", "big",
    "colossal", "enormous", "gigantic", "huge", "immense", "jumbo", "king-size", "large", "massive", "monumental",
    "oversized", "prodigious", "queen-size", "roomy", "spacious", "titanic", "untold", "vast", "wide", "x-large",
    "yawning", "whopping", "aromatic", "biting", "citrusy", "delicious", "earthy", "flavorful", "garlicky", "herbal",
    "juicy", "kicky", "lemony", "minty", "nutty", "oniony", "peppery", "quality", "rich", "savory",
    "tangy", "umami", "vinegary", "woodsy", "yummy", "zesty", "adorable", "beautiful", "cute", "dazzling",
    "elegant", "fancy", "glamorous", "handsome", "irresistible", "jolly", "kittenish", "lovely", "magnificent", "neat",
    "opulent", "pretty", "quaint", "radiant", "sparkling", "trim", "upbeat", "vibrant", "winsome", "xenial",
    "youthful", "zany", "acoustic", "blaring", "chiming", "deafening", "euphonic", "faint", "harmonic", "insistent",
    "jazzy", "lyrical", "melodic", "noisy", "operatic", "piercing", "quiet", "raucous", "sonorous", "thundering",
    "ululating", "vocal", "whispering", "xylophonic", "yodeling", "zingy", "ancient", "bygone", "colonial", "dated",
    "early", "former", "historical", "old", "past", "prehistoric", "primitive", "remote", "retro", "stone-age",
    "traditional", "vintage", "antique", "yesteryear", "zippy", "ample", "bountiful", "copious", "dense", "enough",
    "filled", "generous", "heavy", "infinite", "jam-packed", "lavish", "loaded", "many", "numerous", "overflowing",
    "packed", "quite", "replete", "sufficient", "teeming", "untold", "vast", "whole", "extensive", "yawning",
    "zillion", "adorable", "blissful", "content", "delighted", "ecstatic", "festive", "glad", "happy", "jolly",
    "joyful", "kind", "laughing", "merry", "nice", "optimistic", "pleasant", "quality", "rosy", "smiling",
    "thrilled", "upbeat", "vivacious", "wonderful", "xenial", "yummy", "zany", "authentic", "best", "correct",
    "genuine", "honest", "legitimate", "original", "pure", "real", "right", "true", "valid", "actual",
    "certain", "factual", "for-real", "kosher", "natural", "positive", "precise", "proper", "rightful", "sincere",
    "sound", "sterling", "sure-enough", "true-blue", "unfeigned", "veritable", "well-grounded", "xenial", "yare", "zealous"
]




def random_english_word():
    return random.choice(english_words) + str(np.random.randint(0, 1000000))
def random_num():
    return str(np.random.randint(0, 1000000))