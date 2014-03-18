using System;
using System.Collections.Generic;
using System.Linq;

namespace HundredPrisoners
{
	public class Prisoners
	{
		// These are your input parameters. The default values are sane, though feel
		// free to adjust to play around. n = 3 makes for a good base case.
		private const int N = 100; // The number of prisoners
		private const double RATIO = 0.5; // The probability that a prisoner's value is true

		//
		// This is the function you need to implement.
		//
		// i is the number of this prisoner, from 0 to n-1.
		// dead is a list of booleans for whether or not each previous prisoner died.
		// declared is a list of booleans that each previous prisoner declared.
		//     For both of these lists, the result of the most recent prisoner to go is
		//     the last element, and these lists are both empty for the first prisoner to go.
		// ahead is a list of booleans for all prisoners that the current prisoner can see.
		//     For this list, the next prisoner to go is the first element, and the last
		//     prisoner to go will have an empty ahead list.
		// Returns: The boolean that the current prisoner declares.
		public static bool PrisonerAction(int i, List<bool> dead, List<bool> declared, List<bool> ahead)
		{
			return true;
		}

		// Don't change any code beyond this line. This is the bookkeeping of the simulation.
		#region Simulation
		public static void Main(string[] args)
		{
			Run();
		}

		private static void Run()
		{
			Random random = new Random();
			List<bool> prisoners = new List<bool>(Enumerable.Range(0, N).Select(i => random.NextDouble() < RATIO));
			List<bool> ahead = new List<bool>(prisoners);
			List<bool> dead = new List<bool>();
			List<bool> declared = new List<bool>();

			// The game loop
			for (int i = 0; i < N; i++)
			{
				ahead.RemoveAt(0);
				bool declaration = PrisonerAction(i, dead, declared, ahead);
				declared.Add(declaration);
				dead.Add(declaration != prisoners[i]);
			}

			var numDead = dead.Count(d => d);
			Console.WriteLine("Out of {0} prisoners, you killed {1}.", N, numDead);

			if (numDead > 1 || dead.Skip(1).Count(p => p) != 0)
			{
				Console.WriteLine("You can do better than that!");
			}
			else
			{
				Console.WriteLine("Great job! You found the right algorithm!");
			}
		}
		#endregion
	}
}