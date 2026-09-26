# Feature map contract

Keep a short index beside the app's verification skill. Link one record per feature. Update records when the app changes.

Each record contains:

1. Purpose and visible subfeatures.
2. User entry paths, including keyboard and alternate navigation when supported.
3. Preconditions such as account role, data, flags, and platform.
4. Exact control commands or stable selectors observed in this app.
5. The observable success state and relevant side effects.
6. A failure or boundary case.
7. Recovery and known limitations.
8. Last verification evidence and the revision tested.

Do not invent routes from names. Verify the record against source and a live drive. Mark an inaccessible feature unverified with the missing prerequisite. Feature maps are shared project context, not personal memory.
