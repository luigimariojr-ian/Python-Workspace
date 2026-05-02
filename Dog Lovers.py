print("Welcome to dog lovers!")

print("""
1. Golden retriver
2. Husky
3. Poodle
4. Bulldog
5. German shepherd
      """)

option = int(input("Enter a number from 1 to 5: "))
if option == 1:
    print("Golden Retrievers are a friendly, loyal and highly intelligent breed. They make wonderful pets and are good with children and other animals. They bond with the whole family and anyone else who comes into the house; useless as a guard dog. They have a need to please, making them one of the easiest breeds to train. They perform well in all aspects of competition and enjoy activities such as Flyball, agility and field trials. They love water and are very good swimmers; they are often used by Water Rescuers.")
elif option == 2:
    print("Huskies are energetic and athletic. They are distinguished by their hardiness and cold-weather tolerance, in contrast to many modern sprint sled dogs derived from hound and pointer crossbreeds and purebred sprinting dogs which do not have or retain these qualities. Likewise, they are distinguished from laika, as they were not developed for the primary purpose of hunting game and prey animals.")
elif option == 3:
    print("The Poodle is an active, athletic breed with the varieties differing mostly by size. The FCI's breed standard states the Standard Poodle stands between 45 and 62 centimetres (18 and 24 in), the Medium Poodle between 35 and 45 centimetres (14 and 18 in), the Miniature Poodle between 28 and 35 centimetres (11 and 14 in) and the Toy Poodle 24 and 28 centimetres (9.4 and 11.0 in).")
elif option == 4:
    print("Bulldogs have characteristically wide heads and shoulders along with a pronounced mandibular prognathism. There are generally thick folds of skin on the brow; round, black, wide-set eyes; a short muzzle with characteristic folds called a rope or nose roll above the nose; hanging skin under the neck; drooping lips and pointed teeth, and an underbite with an upturned jaw. The coat is short, flat, and sleek with colours of red, fawn, white, brindle, and piebald. Bulldogs have short tails that can either hang down straight or be tucked in a coiled -corkscrew- into a tail pocket.")
elif option == 5:
    print("German Shepherds are medium to large-sized dogs. The breed standard height at the withers is 60–65 cm (24–26 in) for males, and 55–60 cm (22–24 in) for females. German Shepherds can sprint at speeds of up to 30 miles per hour (48 km/h). German Shepherds are longer than they are tall, with an ideal proportion of 10 to 8+1⁄2. The AKC official breed standard does not set a standard weight range. They have a domed forehead, a long square-cut muzzle with strong jaws and a black nose. The eyes are medium-sized and brown. The ears are large and stand erect, open at the front and parallel, but they often are pulled back during movement. A German Shepherd has a long neck, which is raised when excited and lowered when moving at a fast pace as well as stalking. The tail is bushy and reaches to the hock.")
else:
    print("Invalid Input!")