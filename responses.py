REJECT_TEMPLATE = """Thank you for proposing {title} for inclusion in Interop 2024.

We wanted to let you know that this proposal was not selected to be part of Interop this year.

{reason}

For an overview of our process, see [proposal selection](https://github.com/web-platform-tests/interop/blob/main/2024/selection-process.md). Thank you again for contributing to Interop 2024!

_Posted on behalf of the Interop team._"""

REASONS = {
    "Accept": "This proposal has been accepted as part of Interop 2024!  On behalf of the entire Interop team, thank you for proposing it.  You’ll be able to track progress on this topic throughout the year via the [Interop 2024 dashboard](https://wpt.fyi/interop-2024).",
    "Already Interoperable": "This proposal was not included in Interop 2024 because when we looked at its Web Platform Tests results, we found that it is already largely interoperable between tested browsers and does not need special coordinated attention.",
    "Spec (None)": "The proposal was not on a standards track at the time of proposal selection, which made it unsuitable for inclusion in Interop 2024. Note that this should not be taken as a comment on the technology as a whole, or our willingness to take it up in the future.  If the feature is standardized, we would welcome this proposal being resubmitted for a future round of Interop.",
    "Spec (Incomplete)": "As of the deadline, the specifications for {proposal_name} were not yet complete enough to allow interoperable implementations. To make progress on this area in the future, it will first be necessary to ensure that the feature has a clear specification in a standards track document.",
    "Missing Infrastructure": "We are still missing test infrastructure for testing {proposal_name}. Please note this should not be taken as a comment on the technology as a whole, and once the test infrastructure issues are resolved, we would welcome  this proposal being resubmitted for a future round of Interop.",
    "Missing Tests": "We could not find any tests for {proposal_name} in the Web Platform Tests.  Such tests are crucial for measuring interoperability status and progress.  Once there are WPT entries covering this proposal, we welcome it being resubmitted for a future round of Interop.",
    "Overly Vague or Broad": "We believe this proposal is too broad, and that as such, Interop 2024 is not the right venue to do this {proposal_type}.",
    "Limited Resources / Prioritization": "This is because we got many more proposals than we could include in this year's project. Note that individual vendors may nevertheless choose to advance work in this area during the forthcoming year. We would welcome this proposal being resubmitted again next year if necessary.",
    "(other)": "There are still unresolved issues around {proposal_name}. We would welcome this proposal being resubmitted for a future round of Interop once these issues are resolved.",
    "No consensus": "We did not have consensus to include this proposal. This should not be taken as a comment on the technology as a whole",
}
 
